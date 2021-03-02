import mysql.connector
from datetime import datetime,date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="lucca2021",
    database='testdatabase'
)

myCursor = db.cursor()
# myCursor.execute("INSERT INTO Client (name,phone,address,company) VALUES (%s,%s,%s,%s) ", ('Enrico', 912837123, 'SP', 'ScalaSystems'))
# myCursor.execute("CREATE TABLE `Client` (`name` VARCHAR(50),`phone` INT,`address` VARCHAR(30),`company` VARCHAR(30),`personID` INT NOT NULL AUTO_INCREMENT,PRIMARY KEY (`personID`));")

# myCursor.execute("CREATE TABLE Test (name VARCHAR(50), created datetime)")
# myCursor.execute("INSERT INTO Test (name,created,date) VALUES (%s,%s,%s)",("Lucca",datetime.now(),date.today()))
myCursor.execute("ALTER TABLE Test DROP COLUMN created")
db.commit()

myCursor.execute("SELECT * FROM Test")

for x in myCursor:
    print(x)