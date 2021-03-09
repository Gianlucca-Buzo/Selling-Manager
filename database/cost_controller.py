from database import cursor,db,trip_controller

def insert_cost(costs):
    tripId = trip_controller.get_active_trip()
    if tripId:
        costs.append(tripId)
        cost_values = tuple(costs)
        cursor.execute("INSERT INTO Costs (type,value,description,tripId) VALUES %s" % (cost_values,))
        db.commit()
        return True
    else:
        return False