import mysql.connector as connector

def makeconnection():
    return connector.connect(host='localhost',user='root',password='admin',database='bikedata')