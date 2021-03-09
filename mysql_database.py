from datetime import date
from database import db, cursor

'''
CREATE_CLIENTS = "CREATE TABLE Clients (`clientId` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(50),`phone` INT,`address` VARCHAR(30),`company` VARCHAR(30),PRIMARY KEY (`clientId`)) "
CREATE_TRIPS = "CREATE TABLE Trips (`tripId` int AUTO_INCREMENT,`start_trip` DATE,`end_trip` DATE,`active` BOOLEAN,`total_cost` FLOAT,`clean_profit` FLOAT,`dirty_profit` FLOAT,`origin` VARCHAR(50),`destiny` VARCHAR(50),PRIMARY KEY (tripId))"
CREATE_TRANSACTIONS = "CREATE TABLE `Transactions` (`transactionId` INT AUTO_INCREMENT,`product` VARCHAR(100),`type` VARCHAR(50),`purchase_value` FLOAT,`sale_value` FLOAT,`sale_date` DATE,`quantity` INT,`payment_method` VARCHAR(30),`clientId` INT,tripId INT,PRIMARY KEY (transactionId),FOREIGN KEY (clientId) REFERENCES Clients (clientId),FOREIGN KEY (tripId) REFERENCES Trips (tripId)) "
CREATE_COSTS = "CREATE TABLE Costs (`costId` int AUTO_INCREMENT,`type` VARCHAR(30),`description` VARCHAR(100),`tripId` INT NOT NULL,PRIMARY KEY (costId),FOREIGN KEY(tripId) REFERENCES Trips(tripId))"
'''


class Database:

    def verify_cursor(self,cursor):
        for x in cursor:
            return True
        return False

    def get_active_trip(self):
        cursor.execute("SELECT tripId FROM Trips WHERE active=1")
        for trip in cursor:
            return trip[0]

    def get_client(self, name):
        cursor.execute(f"SELECT clientId FROM Clients WHERE name='{name}'")
        for client in cursor:
            return client[0]

    def start_trip(self, trip_values):
        if not self.exists_active_trip():
            cursor.execute("INSERT INTO Trips (start_trip,active,total_cost,clean_profit,dirty_profit,origin,"
                           "destiny) VALUES %s" % (trip_values,))
            db.commit()
            return True
        else:
            return False

    def end_trip(self,end_trip_date):
        costs_value = self.get_total_cost()
        dirty_profit = self.get_trip_dirty_profit()
        purchase_total_value = self.get_transactions_purchase_value()
        if self.exists_active_trip():
            cursor.execute("UPDATE Trips SET end_trip='%s',dirty_profit='%s',total_cost='%s',clean_profit='%s',"
                           "active='0' WHERE active='1';" % (end_trip_date, dirty_profit, costs_value, dirty_profit -
                                                             (costs_value + purchase_total_value)))
            db.commit()
            return True
        else:
            return False

    def get_trip_id(self):
        cursor.execute("SELECT tripId FROM Trips WHERE active='1'")
        for x in cursor:
            return int(x[0])

    def get_transactions_purchase_value(self):
        cursor.execute("SELECT purchase_value FROM Transactions WHERE tripId='%s'" % (self.get_trip_id(),))
        return self.sum_float_result(cursor)

    def get_trip_dirty_profit(self):
        cursor.execute("SELECT sale_value FROM Transactions WHERE tripId='%s'" % (self.get_trip_id(),))
        return self.sum_float_result(cursor)

    def get_total_cost(self):
        cursor.execute("SELECT value FROM Costs WHERE tripId='%s'" %(self.get_trip_id(),))
        return self.sum_float_result(cursor)

    def sum_float_result(self,cursor):
        total = 0.0
        for x in cursor:
            total += float(x[0])
        return total

    def exists_active_trip(self):
        cursor.execute("SELECT tripId FROM Trips WHERE active='1'")
        return self.verify_cursor(cursor)

    def insert_transaction(self, name, transaction_values, from_trip):
        transaction_values.append(int(self.get_client(name)))
        if from_trip:
            transaction_values.append(self.get_active_trip())
            values_tuple = tuple(transaction_values)
            cursor.execute("INSERT INTO Transactions (product,purchase_value,sale_value,sale_date,quantity,"
                           "payment_method,type,clientId,tripId) VALUES %s" % (values_tuple,))
        else:
            values_tuple = tuple(transaction_values)
            cursor.execute("INSERT INTO Transactions (product,purchase_value,sale_value,sale_date,quantity,"
                           "payment_method,type,clientId) VALUES %s" % (values_tuple,))
        db.commit()

    def insert_client(self, client_values):
        if not self.exists_client(client_values[0]):
            cursor.execute("INSERT INTO Clients (name,phone,address,company,email) VALUES %s" % (client_values,))
            db.commit()
            return True
        else:
            return False

    def exists_client(self, name):
        cursor.execute("SELECT clientId FROM Clients WHERE name = '%s' " % (name,))
        return self.verify_cursor(cursor)

    def insert_cost(self, cost_values):
        cost_values.append(self.get_active_trip())
        cursor.execute("INSERT INTO Costs (type,description,tripId) VALUES %s" % (cost_values,))
        db.commit()

    def get_clients_list(self):
        list = [""]
        cursor.execute("SELECT name FROM Clients")
        for x in cursor:
            list.append(str(x[0]))
        return list



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
