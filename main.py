import mysql.connector as a 
con=a.connect(host="localhost",user="root",passwd="school") 

#Creating databse_&_Tables
c=con.cursor()
D1="create database if not exists library"
c.execute(D1)
A="use school"
c.execute(A)
T1="create table if not exists books(bname varchar(50),bcode varchar(10),total int,subject varchar(50))"
c.execute(T1)
T2="create table if not exists issue (name varchar(50),regno varchar(10),bcode int, issue varchar(50))"
c.execute(T2)
T3="create table if not exists submit(name varchar(50), regno varchar(10),bcode int,submit varchar(50))"
c.execute(T3)
con.commit()

#fun_for_adding_books 

def addbook(): 
 bn=input("Enter the BOOK Name:") 
 c=input("Enter BOOK code:") 
 t=input("Total BOOKS:") 
 s=input("Enter Subject:") 
 data =(bn,c,t,s) 
 sql='insert into books values(%s,%s,%s,%s)' 
 c=con.cursor() 
 c.execute(sql,data) 
 con.commit() 
 print("Data Entered successfully") 
 print("---------------------------------------------------------------------------")
 main() 

 #fun_for_issue_books
  
def issueb(): 
 n=input("Enter the  Name:") 
 r=input("Enter Reg no.:") 
 co=input("Enter book code:") 
 d=input("Enter date:") 
 a='insert into issue values(%s,%s,%s,%s)' 
 data=(n,r,co,d,) 
 c=con.cursor() 
 c.execute(a,data) 
 con.commit() 
 print("Books issued to.",n) 
 print("---------------------------------------------------------------------------")
 bookup(co,-1) 

#fun_for_submit_books
  
def submitb(): 
 n=input("Enter the Name:") 
 r=input("Enter the Reg No.:") 
 co=input("Enter the book code:") 
 d=input("Enter date:") 
 a='insert into submit values(%s,%s,%s,%s)' 
 data=(n,r,co,d,) 
 c=con.cursor() 
 c.execute(a,data) 
 con.commit() 
 print("Books submitted by:",n) 
 print("---------------------------------------------------------------------------")
 bookup(co,+1) 

#fuction_for_update_tables
  
def bookup(co,u): 
 a='select TOTAL from books where BCODE=%s' 
 data=(co,) 
 c=con.cursor() 
 c.execute(a,data) 
 myresult=c.fetchone() 
 t=myresult[0]+u 
 sql="update books set TOTAL=%s where BCODE=%s" 
 d=(t,co) 
 c.execute(sql,d) 
 con.commit() 
 main() 
 
#fun_for_delete_books
 
def dbook(): 
 ac=input("Enter book code:") 
 a='delete from books where BCODE=%s' 
 data =(ac,) 
 c=con.cursor() 
 c.execute(a,data) 
 con.commit() 
 print(ac,"is deleted") 
 main() 
 
 #fuc_for_display_books
 
def dispbook(): 
 a='select * from books' 
 c=con.cursor() 
 c.execute(a) 
 myresult=c.fetchall() 
 for i in myresult: 
  print("Book Name:",i[0]) 
  print("Book Code:",i[1]) 
  print("Total:",i[2]) 
 main() 
 
 
  
#main  
def main():
 print("\n*************") 
 print("\t\t\t\tLIBRARY MANAGER")
 print("*************") 
 print( "1.ADD BOOK") 
 print("2.ISSUE BOOK") 
 print("3.SUBMIT BOOK") 
 print("4.DELETE BOOK") 
 print("5.DISPLAY BOOKS") 
 print("6.EXIT..!!")
 print("\n--------------------------------------------------------")
 choice=int(input("\nEnter task number:"))
 if choice==1: 
  addbook() 
 elif choice==2: 
  issueb() 
 elif choice==3: 
  submitb() 
 elif choice==4: 
  dbook() 
 elif choice==5: 
  dispbook()
 elif choice==6:
  print("----------Thanks For Using Us-------------")
  exit()
 else: 
  print("opp! its a incorrect choice") 
  main()
  
   
#fun_for_passwd 
def pswd():
 print("****Login*****")
 ps=input("Enter the passwd:")
 if ps=='bvm': 
  print("\t\t\t\tSuccessfully Login")
  main()
 else: 
  print(ps," is worng passwd..!!") 
  pswd() 
pswd()