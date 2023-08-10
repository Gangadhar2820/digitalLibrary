#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")


import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')


import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="student_account_details")
mycursor=mydb.cursor()

mycursor.execute("select * from register")
result=mycursor.fetchall()
print("<table border='1'>")
for rows in result:
    print("<tr><td>")
    print(rows)
    print("</td></tr>")
print("</table>")
