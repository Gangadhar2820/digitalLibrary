#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")

import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql as p

import re

import cgi,cgitb

cgitb.enable()

form=cgi.FieldStorage()


bname=form.getvalue('bname')


mydb=p.connect(user="root",host="localhost",password="",database="library_books")

cur=mydb.cursor()

cur.execute("SELECT * FROM book_details")

res=cur.fetchall()

blist=[]

for row in res:
    blist.append(row[0])

bilist=[]



for book in blist:
    
    if book!=None:
        if re.search(bname,book,re.IGNORECASE):
            bilist.append(blist.index(book))



if len(bilist)!=0:
    tab=""
    for i in bilist:
        b=res[i]
        tab+="<tr><td>"+b[0]+"</td>"+"<td>"+b[1]+"</td>"+"<td>"+b[2]+"</td>"+"<td>"+b[3]+"</td>"+"<td>"+b[4]+"</td>"+"<td>"+b[5]+"</td>"+"<td>"+b[6]+"</td></tr>"
    print("<!DOCTYPE html><html><head>")
    print("<style>table{border-collapse:collapse;margin-left:5%;margin-right:5%;width:90%;height:100%;}td{padding:10px;} tr:nth-child(odd){ background-color:rgb(22,194,228,0.2);}</style>")
    print("</head><body>")
    
    print("<table border=2px solid black>")
    print("<tr><th>Title</th><th>Book Id</th><th>Author</th><th>Publisher</th><th>Pages</th><th>Price</th><th>Availability</th></tr>")
    print(tab)
    print("</table></body></html>")



else:
    print("<h2 style='color:red;'>Sorry !,<br> Book with given Name (",bname,") is not available</h2>")
    
        




