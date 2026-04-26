
print("WELCOME TO BANK OF ODISHA")
print()

from database import *
from register import *
from bank import *
from decimal import *

class InputnotMatchError(Exception):
    def __init__(self,msg="Invelid input"):
        self.message=msg
    
    def __str__(self):
        return self.message
    
while True:
    try:
        register=int(input("1. Sign Up\n2. Sign In\n\n"))

        if register==1 or register==2:
            if register==1:
            #Sign-up
                signup()
                break
            else:
            #Sign-in
                username=signin()
                #Give facilities
                if username:
                    b_obj=Bank(username)#so that user can get different fecilities

                    try:
                        choice=int(input("1. BALANCE\n2. DEPOSIT\n3. WITHDRAW\n4. TRANSFER FUNDS\n5. ACCOUNT DETAILS\n6. DELETE ACCOUNT\n7. TRANSACTION HISTORY\n"))

                        cur.execute(f"SELECT account_number FROM customers WHERE username='{username}';")
                        temp_account_number=cur.fetchall()[0][0]

                        cur.execute(f"SELECT secure_pin FROM customers WHERE username='{username}';")
                        temp_secure_pin=cur.fetchall()[0][0]

                        match choice:

                            case 1:
                                #check balance
                                try:
                                    secure_pin=int(input("Enter Secure Pin:"))
                                    if temp_secure_pin==secure_pin:
                                        b_obj.checkbalance(temp_account_number)
                                    else:
                                        print("Incorrect Secure PIN\nEnter your six-digit secure PIN")

                                except ValueError:
                                    print("Incorrect Secure PIN\nEnter your six-digit secure PIN")
                                


                            case 2:
                                #deposit
                                try:
                                    secure_pin=int(input("Enter Secure Pin:"))
                                    if temp_secure_pin==secure_pin:

                                        try:
                                            amount=Decimal(input("Enter Deposit Amount:"))
                                            b_obj.deposit(temp_account_number,amount)
                                        except InvalidOperation:
                                            print("Invelid Deposit Amount")

                                    else:
                                        print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")
                                
                                except ValueError:
                                    print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")


                            case 3:
                                #widrow
                                try:
                                    secure_pin=int(input("Enter Secure Pin:"))
                                    if temp_secure_pin==secure_pin:

                                        try:
                                            amount=Decimal(input("Enter Amount:"))
                                            b_obj.widrow(temp_account_number,amount)
                                        except InvalidOperation:
                                            print("Invelid Withdraw Amount")

                                    else:
                                        print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")
                                except ValueError:
                                    print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")
                                


                            case 4:
                                #transfer fund
                                try:
                                    secure_pin=int(input("Enter Secure Pin:"))
                                    if temp_secure_pin==secure_pin:

                                        try:
                                            reciver_account_number=int(input("Enter Reciver Account Number:"))
                                            if temp_account_number!=reciver_account_number:
                                                cur.execute(f"SELECT account_number FROM customers WHERE account_number='{reciver_account_number}';")
                                                temp=cur.fetchall()
                                                if temp:
                                                    cur.execute(f"SELECT name FROM customers WHERE account_number='{reciver_account_number}';")
                                                    receiver_name=cur.fetchall()[0][0]
                                                    print("Receiver Name:",receiver_name)

                                                    try:
                                                        choice=int(input("1.Confirm\n2.Cancel\n"))
                                                        match choice:
                                                            case 1:

                                                                try:
                                                                    amount=Decimal(input("Enter Amount:"))

                                                                    try:
                                                                        secure_pin=int(input("Enter Secure Pin:"))
                                                                        if temp_secure_pin==secure_pin:
                                                                            b_obj.transferfund(reciver_account_number,receiver_name,temp_account_number,amount)
                                                                        else:
                                                                            print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")
                                                                    
                                                                    except ValueError:
                                                                        print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")

                                                                except InvalidOperation:
                                                                    print("Invelid Amount")

                        
                                                            case 2:
                                                                print("Tranjaction canceled")

                                                            case _:
                                                                raise InputnotMatchError("Invelid Choice Input\n1.Confirm2.Cancel")

                                                    except ValueError:
                                                        print("Invelid Choice Input\n1.Confirm2.Cancel")
                                                    
                                                    except InputnotMatchError as ipe:
                                                        print(ipe)
                                                    
                                                else:
                                                    print("Invelid Account Number")
                                            else:
                                                print("This action can't perform")

                                        except ValueError:
                                            print("Invelid Account Number")

                                    else:
                                        print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")

                                except ValueError:
                                    print("Incorrect Secure Pin\nEnter Your Six digit Secure Pin")


                            case 5:
                                #ACCOUNT DETAILS
                                b_obj.showcustomerdetails()


                            case 6:
                                #DEALETE USER ACCOUNT
                                deleteaccount(username)


                            case 7:
                                #TRANSACTION HISTORY
                                b_obj.transactionhistory()


                            case _:
                                raise InputnotMatchError("1. BALANCE\n2. DEPOSIT\n3. WITHDRAW\n4. TRANSFER FUNDS\n5. ACCOUNT DETAILS\n6. DELETE ACCOUNT\n7. TRANSACTION HISTORY\n")
                            
                    
                    except ValueError as ve:
                        print("1. BALANCE\n2. DEPOSIT\n3. WITHDRAW\n4. TRANSFER FUNDS\n5. ACCOUNT DETAILS\n6. DELETE ACCOUNT\n7. TRANSACTION HISTORY\n")
                    
                    except InputnotMatchError as ipe:
                        print(ipe)
                break #while loop terminate break
        else:
            raise InputnotMatchError("Input not match")
        
    except ValueError:
        print("Invelid Input")
        print()
        print("Enter 1 for Sign-up\nEnter 2 for Sign-in")
        break

    except InputnotMatchError as ipe:
        print(ipe)
        print()
        print("Enter 1 for Sign-up\nEnter 2 for Sign-in")
        break

    # except:
    #     print("\nFailed")
    #     print()
    #     break
    
    finally:
        print("--o--")
    