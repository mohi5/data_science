import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mohit8989$"
) 
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE if not exists test1')