import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mohit8989$"
) 
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mycursor.execute("insert into test1.test_table values(1234,'mohit',432.8)")
mydb.commit()
mydb.close()