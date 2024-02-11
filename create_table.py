import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mohit8989$"
) 
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE if not exists test1.test_table(c1 INT, c2 VARCHAR(60),c3 Float)')
mydb.close()