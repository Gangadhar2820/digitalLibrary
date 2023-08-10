#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")

import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql as p

import cgi,cgitb

cgitb.enable()

form=cgi.FieldStorage()


id1=form.getvalue('id')


mydb=p.connect(user="root",host="localhost",password="",database="library_books")

cur=mydb.cursor()

cur.execute("SELECT * FROM book_details")

res=cur.fetchall()

idlist=[]

for row in res:
    idlist.append(row[1])



if  id1 in idlist:
    ind=idlist.index(id1)
    row=res[ind]


    print("<!DOCTYPE html><html><head>")
    print("<style>table{border-collapse:collapse;margin-left:5%;margin-right:5%;width:90%;height:100%;}td{padding:10px;} tr:nth-child(odd){ background-color:rgb(22,194,228,0.2);}</style>")
    print("</head><body>")
    
    print("<table border=2px solid black>")
    print("<tr><td>Title</td><td>",row[0],"</td></tr>")
    print("<tr><td>Book Id</td><td>",row[1],"</td></tr>")
    print("<tr><td>Author</td><td>",row[2],"</td></tr>")
    print("<tr><td>Publisher</td><td>",row[3],"</td></tr>")
    print("<tr><td>No of pages</td><td>",row[4],"</td></tr>")
    print("<tr><td>Price</td><td>",row[5],"</td></tr>")
    print("<tr><td>Availability</td><td>",row[6],"</td></tr>")
    print("</table>")

    print("</body></html>")
else:
    print("<h2 style='color:red;'>Sorry !,<br> Book with given Id (",id1,") is not available</h2>")
    
        




