import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mohit8989$"
) 
mycursor = mydb.cursor()
# mycursor.execute('select * from test1.test_table')# by this executing this line we are searching for all colums
# For finding specific column we write
mycursor.execute('select c1,c2 from test1.test_table')
for i in mycursor.fetchall():
    print(i)