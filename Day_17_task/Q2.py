#•	Create a employee table and read all the employee name in the table using for loop
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="!123456!",
  database = "rahul"
  )

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Employee1 ( EMP_name VARCHAR(255), EMP_no int , EMP_city VARCHAR(255), EMPdep VARCHAR(255))")
dbse.execute("INSERT INTO Employee ( EMP_name, EMP_no, EMP_city, EMPdep) VALUES  ('John',1033,'DWARKA','IT')")
mydb.commit()

dbse.execute("Show Tables")
for value in dbse:
    print(value)

dbse.execute("SELECT * FROM Employee")

for value in dbse:
    print(value)