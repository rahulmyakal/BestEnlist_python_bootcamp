import mysql.connector

import xlrd

import pandas as pd

mydata = mysql.connector.connect(host="localhost",user="root",passwd="8639488740",database="testdb")

mydb = mydata.cursor()
mydb.execute("create table stu(stdid int primary key,name varchar(30),section char(10))")

loc = ("C:\\Users\\Admin\\Documents\\students.xlsx")
l =list()

a = xlrd.open_workbook(loc)
sheet = a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,5):
    #print(sheet.row_values(i))
    l.append(tuple(sheet.row_values(i)))
#print(l)

# q = "insert into stu(stdid,name,section)values(%s,%s,%s)"
# l = [("6","manee","D")]
# mydb.execute(q,l)
# mydata.commit()
# mydata.close()    

q = "insert into stu(stdid,name,section)values(%s,%s,%s)"
# mydb.executemany(q,l)
# mydata.commit()
mydata.close()    
