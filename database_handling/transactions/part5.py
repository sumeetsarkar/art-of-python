""" Demonstrating psycopg2 transactions

Reference: https://bbengfort.github.io/observations/2017/12/06/psycopg2-transactions.html
"""

import os
import json
import time
import random
from contextlib import contextmanager
from functools import wraps
from threading import Thread

from psycopg2.pool import ThreadedConnectionPool


DIR = os.path.dirname(__file__)
DB_CONFIG = os.path.join(DIR, './config/db-connection.json')

SCHEMA_PATH = os.path.join(DIR, './schema.sql')
FEED_PATH = os.path.join(DIR, './dogfeed.sql')

LEDGER_TYPE_CREDIT = 'credit'
LEDGER_TYPE_DEBIT = 'debit'

def get_db_connection_string(configpath):
    """
    Reads the database config and returns DB connection string
    """
    with open(configpath, 'r') as f:
        config = json.load(f)
        # read keys from json config
        DB_NAME = config['db']
        USER = config['user']
        PASSWORD = config['password']
        # return connection string
        return 'dbname={0} user={1} password={2}'.format(DB_NAME, USER, PASSWORD)


DB_CONN_STRING = get_db_connection_string(DB_CONFIG)


def connect_to_db(connections=2):
    """
    Connect to PostgreSQL and return connection
    """
    minconn = connections
    maxconn = connections * 2
    return ThreadedConnectionPool(minconn, maxconn, DB_CONN_STRING)


# Setup the connection pool
pool = connect_to_db()


@contextmanager
def transaction(name='transaction', *args, **kwargs):
    """
    Generator function, yielding at connection
    Commits/ Rollbacks on success/ exception respectively
    Finally closing the connection
    """
    # Get the session parameters from the kwargs
    options = {
        'isolation_level': kwargs.get('isolation_level', None),
        'readonly': kwargs.get('readonly', None),
        'deferrable': kwargs.get('deferrable', None),
    }
    try:
        conn = pool.getconn()
        conn.set_session(**options)
        yield conn
        conn.commit()
    except Exception as e:
        print('\nROLLBACK TRANSACTION...', e)
        conn.rollback()
        failure_handler = kwargs.get('failure_handler', None)
        failure_handler and failure_handler(**kwargs)
    finally:
        # The method rolls back an eventual pending transaction
        # and executes the PostgreSQL RESET and SET SESSION AUTHORIZATION
        # to revert the session to the default values
        conn.reset()
        pool.putconn(conn)


def transact(options={}):
    def transact_inner(fn):
        """
        This decorator helps in creating a new connection per transaction
        """
        @wraps(fn)
        def wrapper(*args, **kwargs):
            options.update(kwargs)
            with transaction(fn.__name__, *args, **options) as conn:
                fn(conn, *args, **options)
        return wrapper
    return transact_inner


@transact()
def create_schema(conn, schemapath):
    """
    DROP/ CREATE schema from file
    """
    with open(schemapath, 'r') as f:
        sql = f.read()
    with conn.cursor() as curs:
        curs.execute(sql)


@transact()
def dogfeed(conn, feedpath):
    """
    Inserts seed data to users and accounts table
    """
    with open(feedpath, 'r') as f:
        sql = f.read()
    with conn.cursor() as curs:
        curs.execute(sql)


def verify_account(conn, username, accountid):
    """
    Check if userid has matching accountid
    """
    with conn.cursor() as curs:
        sql = (
            'SELECT u.id FROM accounts a JOIN users u on u.id = a.owner_id'
            ' WHERE u.username=%s AND a.id=%s'
        )
        curs.execute(sql, (username, accountid))
        res = curs.fetchone()
        if res is None:
            raise ValueError('\nNo matching user id found for given username and account')
        return res[0]


def authenticate(conn, username, pin, accountid):
    """
    Check for matching userid/ pin in DB
    """
    with conn.cursor() as curs:
        sql = 'SELECT 1 FROM users WHERE username=%s AND pin=%s'
        curs.execute(sql, (username, pin))
        if curs.fetchone() is None:
            raise ValueError('\nUserid/ Pin mismatch')


def ledger_entry(conn, accountid, ledgertype, amount):
    """
    Makes ledger entry for an amount for given userid, accountid & ledgertype (credit/debit)
    """
    with conn.cursor() as curs:
        sql = (
            'INSERT INTO ledger (account_id, type, amount)'
            ' VALUES (%s, %s, %s)'
        )
        res = curs.execute(sql, (accountid, ledgertype, amount))
        if res is not None:
            print('ledger_entry...', res)


def get_balance(conn, userid, accountid):
    """
    Gets account balance for given userid & accountid
    """
    with conn.cursor() as curs:
        sql = ('SELECT balance FROM accounts WHERE owner_id=%s AND id=%s')
        curs.execute(sql, (userid, accountid))
        res = curs.fetchone()
        if res is None:
            raise ValueError('\nNo matching account for userid and accountid')
        return res[0]


def update_balance(conn, userid, accountid, amount):
    """
    Makes deposit to the account
    """
    print('\nUpdating account user:{}, id:{}, amount:{}'.format(userid, accountid, amount))
    with conn.cursor() as curs:
        current = get_balance(conn, userid, accountid)
        sql = (
            'UPDATE accounts'
            ' SET balance=%s'
            ' WHERE owner_id=%s AND id=%s'
        )
        res = curs.execute(sql, (current + amount, userid, accountid))
        if res is not None:
            print('\nupdate_balance', res)
            raise ValueError('\nNo matching account for userid and accountid')


def on_deposit_failure(**kwargs):
    print('\nDEPOSIT failure!!!!', kwargs.get('username', None), str(kwargs.get('amount', None)))


def on_withdraw_failure(**kwargs):
    print('\nWITHDRAW failure!!!!', kwargs.get('username', None), str(kwargs.get('amount', None)))


@transact({
    'isolation_level': 'SERIALIZABLE',
    'failure_handler': on_deposit_failure,
})
def deposit(conn, **kwargs):
    username = kwargs.get('username', None)
    pin = kwargs.get('pin', None)
    accountid = kwargs.get('accountid', None)
    amount = kwargs.get('amount', None)
    # Step 1: authenticate
    authenticate(conn, username, pin, accountid)
    # Step 2: get userid from given username & accountid
    userid = verify_account(conn, username, accountid)
    # Step 3: add ledger entry
    ledger_entry(conn, accountid, LEDGER_TYPE_CREDIT, amount)
    # Step 4: update the account balance
    update_balance(conn, userid, accountid, amount)
    # Step 5: show balance
    balance = get_balance(conn, userid, accountid)
    print('\n{} Deposit: {} , Balance: {}'.format(username, str(amount), str(balance)))


@transact({
    'isolation_level': 'SERIALIZABLE',
    'failure_handler': on_withdraw_failure,
})
def withdraw(conn, **kwargs):
    username = kwargs.get('username', None)
    pin = kwargs.get('pin', None)
    accountid = kwargs.get('accountid', None)
    amount = kwargs.get('amount', None)
    # Step 1: authenticate
    authenticate(conn, username, pin, accountid)
    # Step 2: get userid from given username & accountid
    userid = verify_account(conn, username, accountid)
    # Step 3: add ledger entry
    ledger_entry(conn, accountid, LEDGER_TYPE_DEBIT, amount)
    # Step 4: update the account balance
    update_balance(conn, userid, accountid, amount * -1)
    # Step 5: show balance
    balance = get_balance(conn, userid, accountid)
    print('\n{} Withdraw: {} , Balance: {}'.format(username, str(amount), str(balance)))


def threadedtask(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        t = Thread(target=fn, *args, **kwargs)
        t.start()
    return inner


@threadedtask
def operation1():
    deposit(username='john',
            pin=1234,
            accountid=1,
            amount=20000,
    )
    time.sleep(random.random())
    withdraw(username='john',
            pin=1234,
            accountid=1,
            amount=10000,
    )


@threadedtask
def operation2():
    withdraw(username='john',
            pin=1234,
            accountid=1,
            amount=10000,
    )


def main(options):
    if len(options) > 0 and options[0] == '--flush':
        create_schema(SCHEMA_PATH)
        dogfeed(FEED_PATH)
    operation1()
    operation2()


if __name__ == '__main__':
    options = []
    if len(os.sys.argv) > 1:
        options = os.sys.argv[1: len(os.sys.argv)]
        if options[0] == '--help':
            print("""Usage:
                python part5.py --help
                python part5.py
                python part5.py --flush
            """)
            exit()
    main(options)
