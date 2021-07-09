import json
data =[
    {"name" : "harsh", "id" : "2612", "department" : "IT"},
    {"name" : "kishor", "id" : "8347", "department" : "IT"},
    {"name" : "shrirag", "id" : "3611", "department" : "IT"},
    {"name" : "raviraj", "id" : "5761", "department" : "IT"},
    {"name" : "sai", "id" : "3564", "department" : "IT"}
]

with open("task24t.json","w") as file:
    data= json.dump('task24' , file)
json_string = json.dumps(data)


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!123456!",
    database="mydatabase",
)
task = mydb.cursor()
# task.execute("CREATE TABLE jsondata(name varchar(30), id int , department varchar(50))")
sql = "INSERT INTO jsondata (name,id,department) VALUES (%s,%s,%s)" 
values = json_string
task.execute(sql,values)
mydb.commit()
task.close()