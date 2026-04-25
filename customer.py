#CUSTOMER DETAILS ANDE CREATE USER
from database import *
class Customer:
    def __init__(self,username,password,name,age,address,balance,secure_pin,account_number):
        self.__username=username
        self.__password=password
        self.__name=name
        self.__age=age
        self.__address=address
        self.__balance=balance
        self.__secure_pin=secure_pin
        self.__account_number=account_number
    
    #CREATE USER METHOD
    def createuser(self):
        self.__status=1 
        cur.execute(f"INSERT INTO customers(username,password,name,age,address,balance,secure_pin,account_number,status)VALUES('{self.__username}','{self.__password}','{self.__name}','{self.__age}','{self.__address}','{self.__balance}','{self.__secure_pin}','{self.__account_number}','{self.__status}')")

        mydb.commit()
    
