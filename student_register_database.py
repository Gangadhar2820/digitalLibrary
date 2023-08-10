#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")


import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')


import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
form=cgi.FieldStorage()

name= form.getvalue('sname')
rollno = form.getvalue('rollno')
user=form.getvalue('user')
password=form.getvalue('pass')
cpassword=form.getvalue('cpass')
mail=form.getvalue('mail')

mydb=pymysql.connect(host="localhost",user="root",password="",database="student_account_details")
mycursor=mydb.cursor()

mycursor.execute("select * from register")
result=mycursor.fetchall()
userlist=[]

for row in result:
        userlist.append(row[2])

print(" <!DOCTYPE html>")
print(" <html><head><title>Login Status</title><style>body{background-color:rgb(238,205,163,0.4);font-family:'poppins',sans-serif;}</style></head> <body>")
print("<div style='position:relative;top:100px;text-align:left;box-sizing:border-box;'>")


        
if user not in userlist:
        if password != cpassword:
                print("<h2 style='color:red;'>Password Error: Confirmation Password doesn't matches the Password !</h2>")
                print("<h4><a href='student_register.html'>Click here</a> to Register again.</h4>")
        else:
                con=pymysql.connect(user='root',password='',host='localhost',
                                database='student_account_details')
                cur=con.cursor()
                sql = "INSERT INTO register (name,rollno,userrname,password,mail) VALUES(%s, %s,%s,%s,%s)"
                val = (name,rollno,user,password,mail)
                cur.execute(sql, val)
                con.commit()
                con.close()
                print("<h2 style='color:blue;'>You Successfully Registered !</h2>")
                print("<h3>Username:  <span style='color:red;'>"+user+"</span></h4>")
                print("<h3>Password:  <span style='color:red;'>"+password+"</span></h4>")
                print("<h4><a href='student_login.html'   >Click here</a> to Sign in.</h4>")


else:
    print("<h2 style='color:red;'>Warning: User with  Username("+user+") Already Exists !</h2>")
    print("<h4>Please try another username</h4>")
    print("<h4><a href='student_register.html'>Click here</a> to Register again.</h4>")




print("</div></body></html>")
    












