import pypyodbc

mySQLserver = "127.0.0.1"
myDatabase = "shop"
myUser = "myuser"
myPass = "mypass"

connection = pypyodbc.connect('Driver={PostgreSQL Unicode};'
                              'Server=' + mySQLserver + ';'
                              'Database=' + myDatabase + ';'
                              'uid=' + myUser + ';'
                              'pwd=' + myPass + ';')

cursor = connection.cursor()

mySQLquery = ("""
                select *
                from customer
                
                """)

cursor.execute(mySQLquery)
results = cursor.fetchall()
connection.close()