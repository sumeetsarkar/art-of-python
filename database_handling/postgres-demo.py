import os
import json
import psycopg2


def get_connection_params(configFilePath):
    """Gets database connection string, from reading config params
    Parameters:
      configFilePath (str): Path of the config file containing DB connection parameters
      {
        "db": "",
        "user": "",
        "password": "",
      }
    Returns:
      str: database connection string
    """
    # read file
    with open(configFilePath, 'rt') as f:
        # parse json
        config = json.load(f)
    # read keys from json config
    DB_NAME = config['db']
    USER = config['user']
    PASSWORD = config['password']
    # return connection string
    return 'dbname={0} user={1} password={2}'.format(DB_NAME, USER, PASSWORD)


def connect_to_db(connString):
    """Connects to postgres DB and returns connection
    Parameters:
      connString (str) database connection string
    Returns:
      connection :database connection
    """
    return psycopg2.connect(connString)


def print_db_version(conn):
    """
    Parameters:
      cur (cursor):
    """
    with conn.cursor() as cur:
        cur.execute('SELECT version()')
        dbVersion = cur.fetchone()
        print(dbVersion)


def print_all_employees(conn):
    """
    Parameters:
      cur (cursor):
    """
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM employee')
        rows = cur.fetchall()
        print('Number of results:', cur.rowcount)
        for row in rows:
            print(row)


def init():
    try:
        dirName = os.path.dirname(__file__)
        configFilePath = os.path.join(dirName, './config/db-connection.json')
        connectionString = get_connection_params(configFilePath)
        with connect_to_db(connectionString) as dbConn:
            print('Database connection opened...\n')
            print_db_version(dbConn)
            print_all_employees(dbConn)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# start program
init()
