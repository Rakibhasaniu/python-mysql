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
        INSERT INTO Student(Roll,Name)
        VALUES (1,'John')
"""
mycursor.execute(sqlquery);
mydconnection.commit()
print("inserfewgt3r")