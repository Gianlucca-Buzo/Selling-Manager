from database import cursor, db
import mysql_database as mysql


def get_products_list():
    product_list = [""]
    cursor.execute("SELECT name FROM Products")
    for product in cursor:
        product_list.append(product[0])
    return product_list


def insert_product(name):
    if not exist_product(name):
        cursor.execute(f"INSERT INTO Products (name) VALUES ('{name}')" )
        db.commit()
        return True
    else:
        return False

def delete_product(name):
    if exist_product(name):
        cursor.execute(f"DELETE FROM Products WHERE name='{name}'")
        db.commit()
        return True
    else:
        return False


def exist_product(name):
    cursor.execute(f"SELECT * FROM Products WHERE name='{name}'")
    return mysql.verify_cursor(cursor)


def insert_type(name):
    if not exist_type(name):
        cursor.execute(f"INSERT INTO Types (name) VALUES ('{name}')")
        db.commit()
        return True
    else:
        return False

def delete_type(name):
    if exist_type(name):
        cursor.execute(f"DELETE FROM Types WHERE name='{name}'")
        db.commit()
        return True
    else:
        return False


def exist_type(name):
    cursor.execute(f"SELECT * FROM Types WHERE name='{name}'")
    return mysql.verify_cursor(cursor)


def get_types_list():
    type_list = [""]
    cursor.execute("SELECT name FROM Types")
    for type in cursor:
        type_list.append(type[0])
    return type_list
