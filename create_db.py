import mysql.connector

mydconnection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd="password"
)
print(mydconnection);

db_name = "python_test_db"

mycursor = mydconnection.cursor()

sqlquery = "CREATE DATABASE " + db_name
mycursor.execute(sqlquery);