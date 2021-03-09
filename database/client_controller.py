from database import cursor, db
import mysql_database as mysql


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
