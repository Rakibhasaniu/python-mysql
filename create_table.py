import mysql.connector


db_name = "python_test_db"

mydconnection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd="password",
    database=db_name
)
# print(mydconnection);


mycursor = mydconnection.cursor()

sqlquery = """
    CREATE TABLE Student 
    (
        Roll varchar(4),
        Name varchar(50)
    )
"""
mycursor.execute(sqlquery);