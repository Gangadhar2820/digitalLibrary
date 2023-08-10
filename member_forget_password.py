#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")


import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')


import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
form=cgi.FieldStorage()

mail= form.getvalue('mail')
pass1= form.getvalue('pass1')
cpass=form.getvalue('cpass')

mydb=pymysql.connect(host="localhost",user="root",password="",database="member_account_details")
mycursor=mydb.cursor()

mycursor.execute("select * from member_details")
result=mycursor.fetchall()
membermail=[]



print(" <!DOCTYPE html>")
print(" <html><head><title>Login Status</title><link rel='icon' type='image/x-icon' href='favicon-16x16.png'><style>body{background-color:rgb(253,255,233,0.5);font-family:'poppins',sans-serif;}</style></head> <body>")
print("<div style='position:relative;top:100px;text-align:left;box-sizing:border-box;'>")


for row in result:
        membermail.append(row[3])


        
if mail in membermail:
        old=membermail.index(mail)
        res=result[old]
        old_pass=res[2]
        if pass1 != cpass:
                print("<h3 style='color:red;'>Password Error: <br><br>Confirmation Password doesn't matches the <br><br>New  Password !<br></h2>")
                print("<h4>Please , try again.</h4>")
        else:
                
                EXE="UPDATE  member_details SET password=%s WHERE password=%s"
                VAL=(pass1,old_pass)
                mycursor.execute(EXE,VAL)
                mydb.commit()
                print("<h3>Your Password is Updated Successfully !</h3>")
                print("<h4> <a href='member_login.html' target='_blank'>Click here</a> to Login.</h4>")
                
                


else:
    print("<h3 style='color:red;'>Error : Member With Specified Email is not Exist's  !</h3>")
    print("<h4>Please Check Email.</h4>")
    



print("</div></body></html>")
    












