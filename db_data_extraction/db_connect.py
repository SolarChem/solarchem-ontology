import mysql.connector
from mysql.connector import errorcode
import configparser
import os

parser = configparser.ConfigParser()

conf_file = os.path.join(os.path.dirname(__file__), 'conf', 'settings.conf')
parser.read(conf_file)

config = {
  'user': parser.get("database", "user"),
  'password': parser.get("database", "password"),
  'host': parser.get("database", "host"),
  'database': parser.get("database", "database"),
  'raise_on_warnings': True
}

try:
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

  exit()
else:
  cursor = cnx.cursor()
