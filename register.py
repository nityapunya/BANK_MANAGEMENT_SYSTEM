#USER REGISTRATION SIGNIN, SIGNUP AND DELETE ACCOUNT

# from database import * 
from decimal import Decimal
import random
from customer import *
from bank import *


#SIGN-UP CREATE NEW CUSTOMER RECORD
def signup():
    username=input("Create Username:")
    cur.execute(f"SELECT username FROM customers WHERE username='{username}';")
    temp=cur.fetchall()
    if temp:
        print("User is Already Exists")
        signup()
    else:
        print("User name is Avelaible")
        password=input("Create Password:")
        name=input("Enter your Name:")
        try:
            age=int(input("Enter Age:"))
            address=input("Enter City:")

            while True:
                balance=float(input("Enter Diposit Ammount:"))
                if balance>0:
                    balance=Decimal(balance)
                    break
                else:
                    print("Invelid Deposit Amount")
                    print("Enter Velid Amount")

            while True:
                secure_pin=input("Enter Six digit Secure pin(This Usefull For Account Security):")
                if len(secure_pin)==6:
                    break
                else:
                    print("%s is not six digit"%(secure_pin))

            while True:
                account_number=random.randint(10000000,99999999)
                cur.execute(f"SELECT account_number FROM customers WHERE account_number='{account_number}';")
                temp=cur.fetchall()
                if temp:
                    continue
                else:
                    #create customer
                    c_obj=Customer(username,password,name,age,address,balance,secure_pin,account_number)
                    c_obj.createuser()

                    #create customer Ebook
                    b_obj=Bank(username)
                    b_obj.createebook()
                    
                    #first diposit amount update on username_ebok
                    cur.execute(f"INSERT INTO {username}_ebook VALUES('{today_date}','{today_time}','CR BANK OF ODISHA','','{balance}','{balance}');")
                    mydb.commit()
                    break

        except ValueError:
            print("Invelid Input Age")
        
        else:
            print("Sign-Up Sucessfull")
        
        

#SIGN-IN LOGIN TO BANK
def signin():
    username=input("Enter Username:")

    cur.execute(f"SELECT status FROM customers WHERE username='{username}';")
    status=cur.fetchall()

    if status:
        status=status[0][0]#status will check user is active or not active

    cur.execute(f"SELECT password FROM customers WHERE username='{username}';")
    temp_password=cur.fetchall()

    if status:
        c=1
        while c<=3:
            password=input("Enter Password:")
            if temp_password[0][0]==password:
                print("LOGIN SUCESFULL")
                cur.execute(f"SELECT name FROM customers WHERE password='{password}';")
                name=cur.fetchall()[0][0].upper()
                print("WELCOME {} TO YOUR ACCOUNT".format(name))
                return username
            else:
                c+=1
                print("Incorect Password")
    else:
        print("Invelid Username")

#DELETE ACCOUNT
def deleteaccount(user_name):
    username=input("Enter Your Username:")
    if user_name==username:
        password=input("Enter Password:")
        cur.execute(f"SELECT password FROM customers WHERE username='{user_name}';")
        temp_password=cur.fetchall()[0][0]
        if password==temp_password:
            cur.execute(f"UPDATE customers SET status=0 WHERE username='{user_name}';")
            mydb.commit()
        else:
            print("Incorect Password")
    else:
        print("Invelid Username")
        
                


