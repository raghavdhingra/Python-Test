import cgi
import cgitb
import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='facebookrock',
    database='lol',
    port='3306')
ptr = db.cursor()
form = cgi.fieldstorage()
name = form.getvalue('df')
pwd = form.getpassword('df1')
sql = 'insert into kk (name,lo) values (%s,%s)'
val = (name,pwd)
ptr.execute(sql,val)
db.commit()
