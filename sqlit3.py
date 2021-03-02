import sqlite3

connection = sqlite3.connect('database.sqlite')
cursor = connection.cursor()

# cursor.execute('CREATE TABLE SCHOOL (NAME TEXT NOT NULL, ADDRESS CHAR(50), CITY CHAR(20) NOT NULL, PRODUCT_ID INT)')
cursor.execute("INSERT INTO SCHOOL (NAME,ADDRESS,CITY,PRODUCT_ID) VALUES ('Lucca','General Osorio','Pelotas',1)")
cursor.execute("INSERT INTO SCHOOL (NAME,ADDRESS,CITY,PRODUCT_ID) VALUES ('Isabela','Tres de maio','Pelotas',3)")


connection.commit()
cursor.close()

print("Openned connection successfully")