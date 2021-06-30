import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="Doctors1"
)
dbse = mydb.cursor()
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)