from database import cursor, db,transaction_controller
import mysql_database as mysql
import json


def get_clients_list():
    list = [""]
    cursor.execute("SELECT name FROM Clients")
    for x in cursor:
        list.append(str(x[0]))
    return list


def exists_client(name):
    cursor.execute("SELECT clientId FROM Clients WHERE name = '%s' " % (name,))
    return mysql.verify_cursor(cursor)


def insert_client(client_values):
    if not exists_client(client_values[0]):
        cursor.execute("INSERT INTO Clients (name,phone,address,company,email) VALUES %s" % (client_values,))
        db.commit()
        return True
    else:
        return False


def get_client(name):
    cursor.execute(f"SELECT clientId FROM Clients WHERE name='{name}'")
    for client in cursor:
        return client[0]

def get_clients_data_set():
    names = get_clients_list()[1::]
    dictionare = dict()

    for name in names:
        transactions = transaction_controller.get_transaction_list(name)
        transac_list = []
        for transaction in transactions:
            new_tuple = ("",)
            for itup in transaction:
                new_tuple += (str(itup),)
            transac_list.append(new_tuple)
        dictionare.__setitem__(name,transac_list)

    return dictionare


    # data_set="{ "
    # for name in names:
    #     transactions = transaction_controller.get_transaction_list(name)
    #     transac_list = []
    #     for transaction in transactions:
    #         transac_list.append(str(transaction))
    #     data_set = data_set + f"\"{name}\": {str(transac_list)}, "
    #
    # data_set += "}"

# datas = {
#     "Category 1": [
#         ("New Game 2", "Playnite", "", "", "Never", "Not Played", ""),
#         ("New Game 3", "Playnite", "", "", "Never", "Not Played", ""),
#     ],
#     "No Category": [
#         ("New Game", "Playnite", "", "", "Never", "Not Plated", ""),
#     ]
# }


