from bike import Bike
import connector as c

def getallbikes():
    connection = c.makeconnection()
    stmt = "SELECT bike_id,bike_name,bike_description,bike_model,bike_image,bike_price FROM bike"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(stmt)
    result = cursor.fetchall()
    connection.close()
    return result

def getBike(id):
    connection = c.makeconnection()
    stmt = f"SELECT bike_id,bike_name,bike_description,bike_model,bike_image,bike_price FROM bike WHERE bike_id={id}"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(stmt)
    result = cursor.fetchall()
    connection.close()
    return result

def addBike(b:Bike):
    connection = c.makeconnection()
    stmt = f"INSERT INTO bike(bike_name,bike_description,bike_model,bike_image,bike_price)VALUSE({b.bike_name},{b.bike_desc},{b.bike_model},{b.image},{b.price})"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(stmt)
    connection.commit()
    connection.close()
    return True
    
# print(getallbikes())