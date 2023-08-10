#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql as p
import cgi,cgitb
cgitb.enable()

form=cgi.FieldStorage()
title=form.getvalue('title')
id1=form.getvalue('id')
author=form.getvalue('author')
publisher=form.getvalue('pub')
no=form.getvalue('no')
price=form.getvalue('price')
avail=form.getvalue('avail')

mydb=p.connect(user="root",host="localhost",password="" ,database="library_books")

cur=mydb.cursor()

exe=("INSERT INTO  book_details(title,id,author,publisher,pages,price,avail ) VALUES(%s,%s,%s,%s,%s,%s,%s)")
val=(title,id1,author,publisher,no,price,avail)
cur.execute(exe,val)

mydb.commit()
mydb.close()






