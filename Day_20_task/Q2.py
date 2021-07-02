import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="!123456!",
  database="employee_mangement"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employee")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)