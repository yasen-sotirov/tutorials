"BUILD-IN MODULE SQLITE3"  # https://www.youtube.com/watch?v=Pgov6kpfJMc&list=PLrOQsSoS-V6_4OUM1-9d6x-zTESw_CmeN&index=2&ab_channel=BekBrace

import sqlite3

connection = sqlite3.connect('accounting.db')
cursor = connection.cursor()

sql_command = '''
CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR (20),
    last_name VARCHAR (20),
    gender CHAR,
    joining_date DATE
);'''

cursor.execute(sql_command)


sql_command = '''INSERT INTO employees VALUES (001, "John", "Doe", "M", "2024-04-25")'''
cursor.execute(sql_command)

sql_command = '''INSERT INTO employees VALUES (002, "Ivan", "Todorov", "M", "2024-04-25")'''
cursor.execute(sql_command)

sql_command = '''INSERT INTO employees VALUES (003, "Sarah", "Doe", "M", "2024-05-25")'''
cursor.execute(sql_command)

sql_command = '''INSERT INTO employees VALUES (004, "Noah", "Doe", "M", "2024-06-25")'''
cursor.execute(sql_command)


# Saving changes using commit() method
connection.commit()

# Closing connection
connection.close()


