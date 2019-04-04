import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='facebookrock',
    database='lol',
    port='3306')
cur = db.cursor()
cur1 = db.cursor()
cur1.execute('Select * from kk')
option = input("Are you existing user-(y/n): ")     #10
if option=='y':
    user = input('Enter your username: ')
    if user in cur1:
        pwd = input('Enter Your password: ')
        if pwd in cur1:
            print('Login Successful.......')
        else:
            print('Wrong password.')
    else:
        print('Wrong username.')                    #20
elif option=='n':
    option2 = input('want to create a new account - (y/n): ')
    if option2=='y':
        newuser = input('Enter a new user name: ')
        newpwd = input('Enter a password for it: ')
        sql = "INSERT INTO kk (name,lo) VALUES (%s, %s)"
        val = [
            (newuser,newpwd)
            ]
        cur.executemany(sql, val)
        db.commit() 
    elif option2=='n':                          #30
        exit()
    else:
        print('Type only \'y\' or \'n\'.')
else:
    print('Type only \'y\' or \'n\'.')
