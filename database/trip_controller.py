from database import cursor, db
import mysql_database as mysql


def get_active_trip():
    cursor.execute("SELECT tripId FROM Trips WHERE active=1")
    for trip in cursor:
        return trip[0]
    return 0


def exists_active_trip():
    cursor.execute("SELECT tripId FROM Trips WHERE active='1'")
    return mysql.verify_cursor(cursor)


def start_trip(trip_values):
    if not exists_active_trip():
        cursor.execute("INSERT INTO Trips (start_trip,active,total_cost,clean_profit,dirty_profit,origin,"
                       "destiny) VALUES %s" % (trip_values,))
        db.commit()
        return True
    else:
        return False


def get_total_cost():
    cursor.execute("SELECT value FROM Costs WHERE tripId='%s'" % (get_trip_id(),))
    return mysql.sum_float_result(cursor)


def end_trip(end_trip_date):
    costs_value = get_total_cost()
    dirty_profit = get_trip_dirty_profit()
    purchase_total_value = get_transactions_purchase_value()
    if exists_active_trip():
        cursor.execute("UPDATE Trips SET end_trip='%s',dirty_profit='%s',total_cost='%s',clean_profit='%s',"
                       "active='0' WHERE active='1';" % (end_trip_date, dirty_profit, costs_value, dirty_profit -
                                                         (costs_value + purchase_total_value)))
        db.commit()
        return True
    else:
        return False


def get_trip_id():
    cursor.execute("SELECT tripId FROM Trips WHERE active='1'")
    for x in cursor:
        return int(x[0])


def get_trip_dirty_profit():
    cursor.execute("SELECT sale_value FROM Transactions WHERE tripId='%s'" % (get_trip_id(),))
    return mysql.sum_float_result(cursor)


def get_transactions_purchase_value():
    cursor.execute("SELECT purchase_value FROM Transactions WHERE tripId='%s'" % (get_trip_id(),))
    return mysql.sum_float_result(cursor)
