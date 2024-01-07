import sqlite3

connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE users (ID INTEGER, name TEXT, age INTEGER)")

# cursor.execute("INSERT INTO users VALUES (000001, 'yair' , 56)")
#connection.commit()
cursor.execute("SELECT age FROM users")

result = cursor.fetchall()
print(result)


