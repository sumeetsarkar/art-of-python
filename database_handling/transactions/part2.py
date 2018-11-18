""" Demonstrating psycopg2 transactions

Reference: https://bbengfort.github.io/observations/2017/12/06/psycopg2-transactions.html
"""

import os
import json
from contextlib import contextmanager
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


def create_schema(conn, schemapath):
    """
    DROP/ CREATE schema from file
    """
    with open(schemapath, 'r') as f:
        sql = f.read()
    with conn.cursor() as curs:
        curs.execute(sql)


def dogfeed(conn, feedpath):
    """
    Inserts seed data to users and accounts table
    """
    with open(feedpath, 'r') as f:
        sql = f.read()
    with conn.cursor() as curs:
        curs.execute(sql)


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
    # Operations on a connection is performed by the cursors from connection
    # Every connections starts a new transaction unless committed or rollback
    # So no matter the first cursor performing a execute or subsequent cursor
    # All the executions will not be persisted to Database unless committed

    # By default even a simple SELECT will start a transaction: in long-running programs, 
    # if no further action is taken, the session will remain “idle in transaction”, 
    # an undesirable condition for several reasons (locks are held by the session, tables bloat…). 
    # For long lived scripts, either make sure to terminate a transaction 
    # as soon as possible or use an autocommit connection

    # Here since we created a context manager function transaction,
    # which takes care of the connection to commit or rollback in case of any exception raised
    # and finally close the connection (Essentially returning the connection to a pool, discussed in future parts)
    with transaction() as conn:
        if len(options) > 0 and options[0] == '--flush':
            create_schema(conn, SCHEMA_PATH)
            dogfeed(conn, FEED_PATH)

        # Lists all the users, but also initiates a transaction
        list_users(conn)
        # Still in transaction
        show_accounts(conn, 1)

        # Raises a constraint exception, due to negative amount
        # make_deposit(conn, 1, 'savings', -130.00)

        # current transaction is aborted, commands ignored until end of transaction block
        make_deposit(conn, 1, 'savings', 130.00) # this command, as well as any subsequent command has no effect, a rollback has to be made

        # Rollback needs to be called to end the transaction and start a new one.
        
        make_deposit(conn, 1, 'savings', 150.00)
        # Commit persists the update to database

        # Lists the account statement for user 1, but also initiates a transaction
        show_accounts(conn, 1)



if __name__ == '__main__':
    options = []
    if len(os.sys.argv) > 1:
        options = os.sys.argv[1: len(os.sys.argv)]
        if options[0] == '--help':
            print("""Usage:
                python part2.py --help
                python part2.py
                python part2.py --flush
            """)
            exit()
    main(options)
