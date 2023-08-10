#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")


import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')



import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="abhi")

m = mydb.cursor()

m.execute("CREATE TABLE nagendra (title varchar(30),id varchar(10),author varchar(20),publisher varchar(20),pages varchar(10),price varchar(10),avail varchar(10))")

print("table created successfully")

mydb.close()
