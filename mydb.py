import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Murtazo02!@",

)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE JangoCRM")

print("Database created successfully")



