import mysql.connector

def connect():

  connection = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="",
     database="phishing"
    )
  return connection

