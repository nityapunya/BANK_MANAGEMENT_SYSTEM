#USER ACESS FACILITIES

from database import *
#import date and time module 
import datetime 
dt=datetime.datetime.now()
today_date=dt.strftime("%Y-%m-%d")
today_time=dt.strftime("%I:%M:%S")


class Bank:
    def __init__(self,username):
        self.__username=username

    #USER EBOOK CREATE METHOD
    def createebook(self):
        cur.execute(f"CREATE TABLE IF NOT EXISTS {self.__username}_ebook (date DATE NOT NULL,time TIME NOT NULL,particulars VARCHAR(250) NOT NULL,debit VARCHAR(100),credit VARCHAR(100),balance DECIMAL(10,2))")

        mydb.commit()
    
    #USER BALANCE CHECK METHOD
    def checkbalance(self,account_number):
        cur.execute(f"SELECT balance FROM customers WHERE account_number='{account_number}';")
        balance=cur.fetchall()[0][0]
        print("Avelaible Balance:",balance)
        
    #USER DIPOSIT METHOD
    def deposit(self,account_number,amount):
        if amount>0:
            cur.execute(f"SELECT balance FROM customers WHERE account_number='{account_number}';")
            balance=cur.fetchall()[0][0]
            balance+=amount
            #update for customers table
            cur.execute(f"UPDATE customers SET balance='{balance}' WHERE account_number='{account_number}';")

            #insert record username_ebook
            cur.execute(f"INSERT INTO {self.__username}_ebook VALUES('{today_date}','{today_time}','CR BANK OF ODISHA','','{amount}','{balance}');")
            
            print("Deposit Sucessfull")
            self.checkbalance(account_number)

            mydb.commit()

        else:
            print("Invelid Deposit Amount")

    #USER WIDROW METHOD 
    def widrow(self,account_number,amount):
        cur.execute(f"SELECT balance FROM customers WHERE account_number='{account_number}';")
        balance=cur.fetchall()[0][0]
        if amount>0:
            if amount<=balance:
                balance-=amount
                #update for customer table
                cur.execute(f"UPDATE customers SET balance='{balance}' WHERE account_number='{account_number}';")

                #insert record username_ebook
                cur.execute(f"INSERT INTO {self.__username}_ebook VALUES('{today_date}','{today_time}','DR BANK OF ODISHA','{amount}','','{balance}');")

                print("Widrow Sucessfull")
                self.checkbalance(account_number)

                mydb.commit()
            else:
                print("Insufficient Balance")

        else:
            print("Invelid Withdraw Amount")
    
    #USER TRANSFER MONEY METHOD TO ANOTHER USER
    def transferfund(self,receiver_account_number,receiver_name,sender_account_number,amount):
        if amount>0:
            cur.execute(f"SELECT balance FROM customers WHERE account_number='{sender_account_number}';")
            sender_balance=cur.fetchall()[0][0]
            if amount<=sender_balance:
                #operation for sender
                sender_balance-=amount
                #update for customer table for sender
                cur.execute(f"UPDATE customers SET balance='{sender_balance}' WHERE account_number='{sender_account_number}';")

                #insert record username_ebook for sender
                cur.execute(f"INSERT INTO {self.__username}_ebook VALUES('{today_date}','{today_time}','TRANSFER to {receiver_name} Account Number:{receiver_account_number}','{amount}','','{sender_balance}');")

                #operation for reciver
                cur.execute(f"SELECT balance FROM customers WHERE account_number='{receiver_account_number}';")
                receiver_balance=cur.fetchall()[0][0]
                receiver_balance+=amount

                #update for customer table for receiver
                cur.execute(f"UPDATE customers SET balance='{receiver_balance}' WHERE account_number='{receiver_account_number}';")

                #sender name
                cur.execute(f"SELECT name FROM customers WHERE account_number='{sender_account_number}';")
                sender_name=cur.fetchall()[0][0]

                #receiver username
                cur.execute(f"SELECT username FROM customers WHERE account_number='{receiver_account_number}';")
                receiver_username=cur.fetchall()[0][0]

                #insert record username_ebook for receiver
                cur.execute(f"INSERT INTO {receiver_username}_ebook VALUES('{today_date}','{today_time}','RECIVE FROM {sender_name} Account Number:{sender_account_number}','','{amount}','{receiver_balance}');")

                print("Transfer Sucessfull")
                self.checkbalance(sender_account_number)

                mydb.commit()
            else:
                print("Insufficient Balance")
        else:
            print("Invelid Amount")
    
    #USER SHOW ACCOUNT DETAILS
    def showcustomerdetails(self):
        print("BANK NAME:BANK OF ODISHA")
        cur.execute(f"SELECT * FROM customers WHERE username='{self.__username}';")
        customer_details=cur.fetchall()
        print("USERNAME:",customer_details[0][0])
        print("NAME:",customer_details[0][2])
        print("ACCOUNT NUMBER:",customer_details[0][7])
        print("AGE:",customer_details[0][3])
        print("ADDRESS:",customer_details[0][4])
        print("BALANCE:",customer_details[0][5])