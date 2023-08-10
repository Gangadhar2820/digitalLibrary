#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")


import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')



import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="forget_password")
m = mydb.cursor()
m.execute("CREATE TABLE student_passwords (mail varchar(20),password varchar(20), confirm_password varchar(20))")
print("table created successfully")
mydb.close()
