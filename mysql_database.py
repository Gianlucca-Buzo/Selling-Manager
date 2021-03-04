import mysql.connector
from datetime import datetime, date

def insert_transaction(db,myCursor, values):
    id = 0
    Q3 = f"select personID from Client where name='{values[0]}'"
    myCursor.execute(Q3)
    for x in myCursor:
        id = x[0]
    Q4 = f"insert into Transactions (userId,product,purchase_value,sale_value,sale_date,quantity,payment_method) " \
         f"VALUES ({id},'{values[1]}','{values[2]}','{values[3]}','{values[4]}','{values[5]}') "
    myCursor.execute(Q4)
    db.commit()

    for x in myCursor:
        print(x)

def insert_client(db,myCursor,values):
    Query_insert = "INSERT INTO Client (name,phone,address,company) VALUES (%s,%s,%s,%s)",(values[0],values[1],values[2],values[3])

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="lucca2021",
    database='testdatabase'
)

myCursor = db.cursor()
# myCursor.execute("INSERT INTO Client (name,phone,address,company) VALUES (%s,%s,%s,%s) ", ('Enrico', 912837123, 'SP', 'ScalaSystems'))
# myCursor.execute("CREATE TABLE 'Client' ('name' VARCHAR(50),'phone' INT,'address' VARCHAR(30),'company' VARCHAR(30),'personID' INT NOT NULL AUTO_INCREMENT,PRIMARY KEY ('personID'));")

# myCursor.execute("CREATE TABLE Test (name VARCHAR(50), created datetime)")
# myCursor.execute("INSERT INTO Test (name,created,date) VALUES (%s,%s,%s)",("Lucca",datetime.now(),date.today()))
# myCursor.execute("ALTER TABLE Test DROP COLUMN created")
# db.commit()
#
# myCursor.execute("SELECT * FROM Test")


Q1 = "CREATE TABLE Client ('name' VARCHAR(50),'phone' INT,'address' VARCHAR(30),'company' VARCHAR(30),'personID' INT " \
     "NOT NULL AUTO_INCREMENT,PRIMARY KEY ('personID') "
Q2 = "CREATE TABLE `Transactions` (`userId` INT,`product` VARCHAR(100),`purchase_value` DECIMAL,`sale_value` DECIMAL," \
     "`sale_date` DATE,`quantity` INT,`payment_method` VARCHAR(30),PRIMARY KEY (userId),FOREIGN KEY (userId) " \
     "REFERENCES Client (personID)); "

Q3 = "select * from Transactions"

Q4 = "CREATE TABLE Trips ('tripId' int AUTO_INCREMENT, 'start_trip DATE','end_trip DATE','active', PRIMARY KEY (tripId))"

values = ['Enrico', 'Palmito','10.5','15.5',date.today(),'10','Dinheiro']
insert_transaction(db,myCursor,values)
myCursor.execute(Q3)


for x in myCursor:
    print(x[0])



