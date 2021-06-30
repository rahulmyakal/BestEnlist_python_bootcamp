import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
print(mydb)
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Doctors1")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)



dbse.execute("CREATE TABLE Doctors (dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
('doctors',)
dbse = mydb.cursor()

sql = "INSERT INTO Doctors (dr_id , Patient_visited) VALUES (%s,%s)"
val = [
  ('DID1','10'),
    ('DID2','3'),
    ('DID3','8'),
    ('DID5','0'),
    ('DID123','15'),
    ('DID26','9'),
    ('DID78','0'),
    ('DID65','0'),
     ('DID23','15'),
    ('DID262','9'),
    ('DID783','0'),
    ('DID651','0'), 
    ('DID13','19'),
    ('DID267','7'),
    ('DID8','0'),
    ('DID59','0')    
]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")
