#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: type/html\n\n")

import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql as p

md=p.connect(host="localhost",user="root",password="",database="library_books")

cur=md.cursor()

l=["java"]


for i in l:
    cur.execute("DELETE FROM book_details WHERE  id=%s",i)

    
print("Completed")

md.commit()
