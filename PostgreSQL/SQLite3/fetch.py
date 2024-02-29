import sqlite3
connection = sqlite3.connect('accounting.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM employees')

data = cursor.fetchall()
print(data)

cursor.execute('SELECT * FROM employees WHERE joining_date == "2024-04-25"')
data = cursor.fetchall()
print(data)



