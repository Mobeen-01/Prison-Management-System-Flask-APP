import sqlite3 as sql


conn = sql.connect('database.db')
# print ("Opened database successfully")

# conn.execute('CREATE TABLE Product (productID INTEGER PRIMARY KEY, productName TEXT ,productDescription TEXT,QTY INTEGER)')
# print ("Table Product Done")

# conn.execute('CREATE TABLE locations (locationID INTEGER PRIMARY KEY, locationName TEXT)')
# print ("Table location Done")

conn.execute('UPDATE TABLE product_movement (movementID INTEGER PRIMARY KEY, productName TEXT, Timing timestamp, fromlocation TEXT, tolocation TEXT,QTY INTEGER)')
print ("Table productmovement Done")

conn.execute("INSERT INTO Balance (locationName,productName,QTY)VALUES('Mumbai','STEEL','10')")
print ("Table balance c successfully")