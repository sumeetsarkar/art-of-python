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
  fileR = open(configFilePath, 'rt')
  # parse json
  config = json.loads(fileR.read())
  fileR.close()
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


def print_db_version(cur):
  """
  Parameters:
    cur (cursor):
  """
  cur.execute('SELECT version()')
  dbVersion = cur.fetchone()
  print(dbVersion)
  cur.close()


def print_all_employees(cur):
  """
  Parameters:
    cur (cursor):
  """
  cur.execute('SELECT * FROM employee')
  rows = cur.fetchall()
  print('Number of results:', cur.rowcount)
  for row in rows:
    print(row)
  cur.close()


def init():
  try:
    dirName = os.path.dirname(__file__)
    configFilePath = os.path.join(dirName, './config/db-connection.json')
    connectionString = get_connection_params(configFilePath)
    dbConn = connect_to_db(connectionString)
    print('Database connection opened...\n')
    print_db_version(dbConn.cursor())
    print_all_employees(dbConn.cursor())
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if dbConn is not None:
      dbConn.close()
      print('\nDatabase connection closed...')


# start program
init()
