#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")


import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')
import cgi, cgitb
import pymysql
cgitb.enable()
form=cgi.FieldStorage()
mydb=pymysql.connect(host="localhost",user="root",password="",database="student_account_details")
mycursor=mydb.cursor()

mycursor.execute("select * from register")
result=mycursor.fetchall()
userlist=[]

for row in result:
        userlist.append(row[2])

username = form.getvalue('uname')
password = form.getvalue('pass')

print(" <!DOCTYPE html>")
print(" <html><head><title>Login Status</title><link rel='icon' type='image/x-icon' href='favicon-16x16.png'><style>body{background-color:rgb(253,255,233,0.5);font-family:'poppins',sans-serif;}</style></head> <body>")
print("<div style='position:relative;top:100px;text-align:left;box-sizing:border-box;'>")



if username in userlist:
     i=userlist.index(username)
     row=result[i]
     if(row[3]==password):
         print("<h2 style='color:blue;opacity:0.7;margin-left:50px;'>Account Validation Success.</h2>")
         print("<h2 style='color:;opacity:0.7;margin-left:50px;'>Welcome , "+row[0]+" !</h2>")
         print("<h4 style='color:;opacity:0.7;margin-left:50px;'><a href='student_home_page.html' target='_blank'  >Click here  </a>to Sign in.</h4>")
     else:
         print("<h2 style='color:red;opacity:0.7;margin-left:50px;'>Error:Invalid Password!</h2>")
         print("<h4 style='color:;opacity:0.7;margin-left:50px;'>Please, Check Password</h4>")
         print("<h4 style='color:;opacity:0.7;margin-left:50px;'>If you forget password.Click forget password</h4>")
        
else:
    print("<h2 style='color:red;opacity:0.7;margin-left:50px;'>Error:User Doesn't Exist!</h2>")
    print("<h4 style='color:;opacity:0.7;margin-left:50px;'>Please  try to Login again.</h4>")
    print("<h4 style='color:;opacity:0.7;margin-left:50px;'>If you are New. Please Register</h4>")


   
print("</div></body></html>  ")


     
    











    

