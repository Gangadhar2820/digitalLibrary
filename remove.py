#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: type/html\n\n")

import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql as p

import cgi,cgitb

cgitb.enable()


form=cgi.FieldStorage()

hall=form.getvalue('hall')

md=p.connect(host="localhost",user="root",password="",database="student_account_details")

cur=md.cursor()

cur.execute("DELETE FROM register WHERE  rollno=%s",hall)


md.commit()
