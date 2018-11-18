""" Demonstrating psycopg2 transactions

Reference: https://bbengfort.github.io/observations/2017/12/06/psycopg2-transactions.html
"""

import os
import json
from contextlib import contextmanager
from functools import wraps
import psycopg2 as pg

DIR = os.path.dirname(__file__)
DB_CONFIG = os.path.join(DIR, './config/db-connection.json')

SCHEMA_PATH = os.path.join(DIR, './schema.sql')
FEED_PATH = os.path.join(DIR, './dogfeed.sql')

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


def connect_to_db():
    """
    Connect to PostgreSQL and return connection
    """
    return pg.connect(DB_CONN_STRING)


@contextmanager
def transaction():
    """
    Generator function, yielding at connection
    Commits/ Rollbacks on success/ exception respectively
    Finally closing the connection
    """
    try:
        conn = connect_to_db()
        yield conn
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def transact(fn):
    """
    This decorator helps in creating a new connection per transaction
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        with transaction() as conn:
            fn(conn, *args, **kwargs)
    return wrapper


@transact
def create_schema(conn, schemapath):
    """
    DROP/ CREATE schema from file
    """
    with open(schemapath, 'r') as f:
        sql = f.read()
    with conn.cursor() as curs:
        curs.execute(sql)


@transact
def dogfeed(conn, feedpath):
    """
    Inserts seed data to users and accounts table
    """
    with open(feedpath, 'r') as f:
        sql = f.read()
    with conn.cursor() as curs:
        curs.execute(sql)


@transact
def make_deposit(conn, userid, acctype, amount):
    """
    Makes deposit to the account
    """
    print('\n\nUpdating account user:{}, type:{}, amount:{}'.format(userid, acctype, amount))
    with conn.cursor() as curs:
        res = curs.execute("""UPDATE accounts
                                SET balance=%s
                                WHERE owner_id=%s AND type=%s""", (amount, userid, acctype))
        if res is not None:
            print(res)


@transact
def list_users(conn):
    """
    List all users
    """
    print('\n\nListing all users')
    with conn.cursor() as curs:
        curs.execute('SELECT * from users')
        rows = curs.fetchall()
        print('Number of results:', curs.rowcount)
        for row in rows:
            print(row)


@transact
def show_accounts(conn, userid):
    """
    Lists account statement for a given userid
    """
    print('\n\nAccount statment for user', (userid))
    with conn.cursor() as curs:
        curs.execute('SELECT id, type, balance FROM accounts WHERE owner_id=%s', (userid,))
        rows = curs.fetchall()
        print('Number of results:', curs.rowcount)
        for row in rows:
            print(row)


def main(options):
    if len(options) > 0 and options[0] == '--flush':
        create_schema(SCHEMA_PATH)
        dogfeed(FEED_PATH)

    # Since each of the below function definitions is decorated with @transact,
    # each of the performs its database operation in its own transaction, i.e., its own connection
    list_users()
    show_accounts(1)
    make_deposit(1, 'savings', 130.00)
    show_accounts(1)
    # As a result, the following make_deposit causing a Constraint Exception 
    # does not effect the following transactions, as this exception is rolled back
    # and the connection is released
    make_deposit(1, 'savings', -130.00)
    show_accounts(1)
    make_deposit(1, 'savings', 150.00)
    show_accounts(1)



if __name__ == '__main__':
    options = []
    if len(os.sys.argv) > 1:
        options = os.sys.argv[1: len(os.sys.argv)]
        if options[0] == '--help':
            print("""Usage:
                python part3.py --help
                python part3.py
                python part3.py --flush
            """)
            exit()
    main(options)
