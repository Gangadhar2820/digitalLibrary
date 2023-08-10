#!C:/Program Files (x86)/Python38-32/python.exe
print("Content-Type: text/html\n\n")

import sys

sys.path.append("c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages")

import pymysql

mydb=pymysql.connect( user="root", host="localhost" ,password="",database="student_account_details")

c=mydb.cursor()

EXE="UPDATE  register SET password=%s WHERE password=%s"
VAL=('hai','HAI')
c.execute(EXE,VAL)

mydb.commit()


