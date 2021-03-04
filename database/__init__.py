import mysql.connector

db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="lucca2021",
            database='testdatabase'
        )
cursor = db.cursor()

# class Database:
#
#     def __init__(self):



