#USER REGISTRATION SIGNIN, SIGNUP AND DELETE ACCOUNT
 
from decimal import Decimal
import random
from customer import *
from bank import *


#SIGN-UP CREATE NEW CUSTOMER RECORD
def signup():
    username=input("Enter a username: ")
    cur.execute(f"SELECT username FROM customers WHERE username='{username}';")
    temp=cur.fetchall()
    if temp:
        print("Username already exists")
        signup()
    else:
        print("Username is available")
        password=input("Create a password: ")
        name=input("Enter your name: ")
        try:
            age=int(input("Enter your age: "))
            address=input("Enter your city: ")

            while True:
                try:
                    balance=float(input("Enter deposit amount: "))
                    if balance>0:
                        balance=Decimal(balance)
                        break
                    else:
                        print("Invalid deposit amount. Enter a value greater than 0.")

                except ValueError:
                    print("Invalid deposit input")

            while True:
                secure_pin=input("Enter a 6-digit secure PIN: ")
                if len(secure_pin)==6:
                    break
                else:
                    print(f"{secure_pin} is not a 6-digit PIN")

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
            print("Invalid input for age")
        
        else:
            print("Sign-up successful")
            print("Account created successfully")
            print(f"Your account number is: {account_number}")
        
        

#SIGN-IN LOGIN TO BANK
def signin():
    username=input("Enter username: ")

    cur.execute(f"SELECT status FROM customers WHERE username='{username}';")
    status=cur.fetchall()

    if status:
        status=status[0][0]#status will check user is active or not active

    cur.execute(f"SELECT password FROM customers WHERE username='{username}';")
    temp_password=cur.fetchall()

    if status:
        c=1
        while c<=3:
            password=input("Enter password: ")
            if temp_password[0][0]==password:
                print("Login successful")
                cur.execute(f"SELECT name FROM customers WHERE password='{password}';")
                name=cur.fetchall()[0][0].upper()
                print(f"Welcome to your account, {name}")
                return username
            else:
                c+=1
                print("Incorrect password")
    else:
        print("Invalid username")

#DELETE ACCOUNT
def deleteaccount(user_name):
    username=input("Enter your username: ")
    if user_name==username:
        password=input("Enter your password: ")
        cur.execute(f"SELECT password FROM customers WHERE username='{user_name}';")
        temp_password=cur.fetchall()[0][0]
        if password==temp_password:
            cur.execute(f"UPDATE customers SET status=0 WHERE username='{user_name}';")
            mydb.commit()
        else:
            print("Incorrect password")
    else:
        print("Invalid username")
        
                


