import json
import psycopg2

def get_connection_params():
  fileR = open('./config/db-connection.json', 'rt')
  config = json.loads(fileR.read())
  DB_NAME = config['db']
  USER = config['user']
  PASSWORD = config['password']
  fileR.close()
  return 'dbname={0} user={1} password={2}'.format(DB_NAME, USER, PASSWORD)

def connect_to_db(params):
  return psycopg2.connect(params)

def print_db_version(cur):
  cur.execute('SELECT version()')
  dbVersion = cur.fetchone()
  print(dbVersion)
  cur.close()

def execute_statements(cur):
  cur.execute('SELECT * FROM employee')
  rows = cur.fetchall()
  print('Number of results:', cur.rowcount)
  for row in rows:
    print(row)
  cur.close()

def init():
  try:
    dbConn = connect_to_db(get_connection_params())
    print('Database connection opened...\n')
    print_db_version(dbConn.cursor())
    execute_statements(dbConn.cursor())
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if dbConn is not None:
      dbConn.close()
      print('\nDatabase connection closed...')

init()
