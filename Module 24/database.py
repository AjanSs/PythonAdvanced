import sqlite3

from Module5.defaultArguments import custom_greeting

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        department TEEXT NOT NULL,
        salary REAL
    
    )  

''')

#Commit the changes

connection.commit()

cursor.execute('''
    INSERT INTO employees (name,position,department,salary)
    VALUES (?,?,?,?)
''',('John Doe','Software Engineer','IT',7000.00))

connection.commit()

cursor.execute('SELECT * FROM employees')

#Fetch all results
rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute('''
    UPDATE employees
    SET SALARY = ?
    WHERE name = ?
''',(7500.00,'John Doe'))

connection.commit()

#ursor.execute('SELECT * FROM employees')

#Fetch all results
#rows = cursor.fetchall()

#for row in rows:
#    print(row)

cursor.execute('''
    DELETE FROM employees
    WHERE name = ?
''',('John Doe',))

connection.commit()


cursor.close()
connection.close()