#•	Create a employee table and read all the employee name in the table using for loop
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="!123456!",
  database = "rahul"
  )

dbse = mydb.cursor()
dbse.excute("CREATE TABLE Employee ( EMP_name VARCHAR(255), EMP_no int , EMP_city VARCHAR(255), EMPdep VARCHAR(255))")
dbse.excute("Show Tables")
for value in dbse:
    print(value)