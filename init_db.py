import sqlite3

# creating a db file
connection = sqlite3.connect('app.db')

# creating a cursor to execute SQL commands
db_cursor = connection.cursor()

# adding info to tables
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        course_group TEXT NOT NULL
    )
''')

# updating the db with data
connection.commit()
connection.close()

