#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="manohar"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE std (name VARCHAR(25), age VARCHAR(2))")
mydb.commit()
print("table created successfully")
mydb.close()
