import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="facebookrock",
  port='3306',
  database="lol"
)

mycursor = mydb.cursor()

sql = "INSERT INTO kk (name, lo) VALUES (%s, %s)"
val = [("Michelle", "Blue V")]
mycursor.executemany(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
