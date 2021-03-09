from datetime import date
from database import db, cursor
import database.trip_controller as trip

'''
CREATE_CLIENTS = "CREATE TABLE Clients (`clientId` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(50),`phone` INT,`address` VARCHAR(30),`company` VARCHAR(30),PRIMARY KEY (`clientId`)) "
CREATE_TRIPS = "CREATE TABLE Trips (`tripId` int AUTO_INCREMENT,`start_trip` DATE,`end_trip` DATE,`active` BOOLEAN,`total_cost` FLOAT,`clean_profit` FLOAT,`dirty_profit` FLOAT,`origin` VARCHAR(50),`destiny` VARCHAR(50),PRIMARY KEY (tripId))"
CREATE_TRANSACTIONS = "CREATE TABLE `Transactions` (`transactionId` INT AUTO_INCREMENT,`product` VARCHAR(100),`type` VARCHAR(50),`purchase_value` FLOAT,`sale_value` FLOAT,`sale_date` DATE,`quantity` INT,`payment_method` VARCHAR(30),`clientId` INT,tripId INT,PRIMARY KEY (transactionId),FOREIGN KEY (clientId) REFERENCES Clients (clientId),FOREIGN KEY (tripId) REFERENCES Trips (tripId)) "
CREATE_COSTS = "CREATE TABLE Costs (`costId` int AUTO_INCREMENT,`type` VARCHAR(30),`description` VARCHAR(100),`tripId` INT NOT NULL,PRIMARY KEY (costId),FOREIGN KEY(tripId) REFERENCES Trips(tripId))"
'''


def sum_float_result(cursor):
    total = 0.0
    for x in cursor:
        total += float(x[0])
    return total


def verify_cursor(cursor):
    for x in cursor:
        return True
    return False


# if __name__ == '__main__':
#     values = ['Enrico', 'Palmito', '10.5', '15.5', date.today(), '10', 'Dinheiro']
#     # values = ("Enrico",53981312377,"Pelotas","Centauro")
#     # myCursor.execute(insert_client(values))
#     # db.commit()
#     insert_transaction(values)
#     cursor.execute("SELECT * FROM Clients")
#
#     List = []
#     for x in cursor:
#         print(x)
#         List.append(x)
#
#     print(f"Lista: {List}")
