import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='facebookrock',
    database='lol',
    port='3306')
cur1 = db.cursor()
sql = 'Select * from kk where (name =x %s)'
oop = input()
val = (oop)
cur1.execute(sql,val)
for i in cur1:
    print(i)
