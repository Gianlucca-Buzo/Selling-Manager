from database import cursor,db
from database import trip_controller,client_controller

def insert_transaction(name, transaction_values, from_trip):
    transaction_values.append(int(client_controller.get_client(name)))
    if from_trip:
        transaction_values.append(trip_controller.get_active_trip())
        values_tuple = tuple(transaction_values)
        cursor.execute("INSERT INTO Transactions (product,purchase_value,sale_value,sale_date,quantity,"
                       "payment_method,type,clientId,tripId) VALUES %s" % (values_tuple,))
    else:
        values_tuple = tuple(transaction_values)
        cursor.execute("INSERT INTO Transactions (product,purchase_value,sale_value,sale_date,quantity,"
                       "payment_method,type,clientId) VALUES %s" % (values_tuple,))
    db.commit()