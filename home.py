print()
print("=== Welcome to Bank of Odisha ===")
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
        register=int(input("1. Sign Up\n2. Sign In\n\nEnter your choice: "))

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
                        choice=int(input("\n=== Select an Option ===\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transfer Funds\n5. Account Details\n6. Delete Account\n7. Transaction History\n\nEnter your choice: "))

                        cur.execute(f"SELECT account_number FROM customers WHERE username='{username}';")
                        temp_account_number=cur.fetchall()[0][0]

                        cur.execute(f"SELECT secure_pin FROM customers WHERE username='{username}';")
                        temp_secure_pin=cur.fetchall()[0][0]

                        match choice:

                            case 1:
                                #check balance
                                try:
                                    secure_pin=int(input("Enter secure PIN: "))
                                    if temp_secure_pin==secure_pin:
                                        b_obj.checkbalance(temp_account_number)
                                    else:
                                        print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")

                                except ValueError:
                                    print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")
                                


                            case 2:
                                #deposit
                                try:
                                    secure_pin=int(input("Enter secure PIN: "))
                                    if temp_secure_pin==secure_pin:

                                        try:
                                            amount=Decimal(input("Enter deposit amount: "))
                                            b_obj.deposit(temp_account_number,amount)
                                        except InvalidOperation:
                                            print("Invalid deposit amount.")

                                    else:
                                        print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")
                                
                                except ValueError:
                                    print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")


                            case 3:
                                #widrow
                                try:
                                    secure_pin=int(input("Enter secure PIN: "))
                                    if temp_secure_pin==secure_pin:

                                        try:
                                            amount=Decimal(input("Enter withdrawal amount: "))
                                            b_obj.widrow(temp_account_number,amount)
                                        except InvalidOperation:
                                            print("Invalid withdrawal amount.")

                                    else:
                                        print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")
                                except ValueError:
                                    print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")
                                


                            case 4:
                                #transfer fund
                                try:
                                    secure_pin=int(input("Enter secure PIN: "))
                                    if temp_secure_pin==secure_pin:

                                        try:
                                            reciver_account_number=int(input("Enter receiver account number: "))
                                            if temp_account_number!=reciver_account_number:
                                                cur.execute(f"SELECT account_number FROM customers WHERE account_number='{reciver_account_number}';")
                                                temp=cur.fetchall()
                                                if temp:
                                                    cur.execute(f"SELECT status FROM customers WHERE account_number='{reciver_account_number}'; ")
                                                    status=cur.fetchall()[0][0]

                                                    if status:
                                                        cur.execute(f"SELECT name FROM customers WHERE account_number='{reciver_account_number}';")
                                                        receiver_name=cur.fetchall()[0][0]
                                                        print("Receiver name:", receiver_name)

                                                        try:
                                                            choice=int(input("1. Confirm\n2. Cancel\n\nEnter your choice: "))
                                                            match choice:
                                                                case 1:

                                                                    try:
                                                                        amount=Decimal(input("Enter transfer amount: "))

                                                                        try:
                                                                            secure_pin=int(input("Enter secure PIN: "))
                                                                            if temp_secure_pin==secure_pin:
                                                                                b_obj.transferfund(reciver_account_number,receiver_name,temp_account_number,amount)
                                                                            else:
                                                                                print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")
                                                                        
                                                                        except ValueError:
                                                                            print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")

                                                                    except InvalidOperation:
                                                                        print("Invelid Amount")

                            
                                                                case 2:
                                                                    print("Transaction cancelled.")

                                                                case _:
                                                                    raise InputnotMatchError("Invalid choice input.\n1. Confirm\n2. Cancel")

                                                        except ValueError:
                                                            print("Invalid choice input.\n1. Confirm\n2. Cancel")
                                                        
                                                        except InputnotMatchError as ipe:
                                                            print(ipe)
                                                    else:
                                                        print("Invalid account number.")
                                                else:
                                                    print("Invalid account number.")
                                            else:
                                                print("This action cannot be performed.")

                                        except ValueError:
                                            print("Invelid Account Number")

                                    else:
                                        print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")

                                except ValueError:
                                    print("Incorrect secure PIN.\nPlease enter your 6-digit secure PIN.")


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
                                raise InputnotMatchError("Invalid choice input.\n1. Balance\n2. Deposit\n3. Withdraw\n4. Transfer Funds\n5. Account Details\n6. Delete Account\n7. Transaction History")
                            
                    
                    except ValueError as ve:
                        print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transfer Funds\n5. Account Details\n6. Delete Account\n7. Transaction History")
                    
                    except InputnotMatchError as ipe:
                        print(ipe)
                break #while loop terminate break
        else:
            raise InputnotMatchError("Input not match")
        
    except ValueError:
        print("Invelid Input")
        print()
        print("1. Sign Up\n2. Sign In")
        break

    except InputnotMatchError as ipe:
        print(ipe)
        print()
        print("1. Sign Up\n2. Sign In")
        break

    except:
        print("\nFailed")
        print()
        break
    
    finally:
        print("--o--")
    