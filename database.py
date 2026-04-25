#BANKING DATABASE
import mysql.connector as sql
mydb=sql.connect(
    host="localhost",
    user="root",
    password="nitya@756029",
    database="BANK"
    )
cur=mydb.cursor()
def createcustomertable():#CREATE CUSTOMER TABLE
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS customers (username VARCHAR(210) NOT NULL,password VARCHAR(210) NOT NULL,name VARCHAR(210) NOT NULL,age INT NOT NULL,address VARCHAR(210) NOT NULL,balance DECIMAL(10,2) NOT NULL,secure_pin INT NOT NULL,account_number INT NOT NULL,status BOOLEAN NOT NULL)"
    )
mydb.commit()

if __name__=="__main__":
    createcustomertable()