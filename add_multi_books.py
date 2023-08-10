#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: type/html\n\n")

import sys
sys.path.append('c:\\users\\rgang\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql as p

md=p.connect(host="localhost",user="root",password="",database="library_books")

cur=md.cursor()

n=int(input("Enter No of books you want to add : "))

for i in range(1,n+1):
    print("\n\tEnter book",i,"details:\n")
    t=input("\tTitle               :  ")
    i=input("\tId                   :  ")
    a=input("\tAuthor           :  ")
    p=input("\tPublisher        :  ")
    c=input("\tPages              :  ")
    d=input("\tPrice               :  ")
    e=input("\tAvailability     :  ")

    cur.execute("INSERT INTO  book_details(title,id,author,publisher,pages,price,avail) VALUES(%s,%s,%s,%s,%s,%s,%s)",(t,i,a,p,c,d,e))
    md.commit()

print("you successfully added ",n,"books into database")
    
    
