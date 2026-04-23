import sqlite3

# Database file name
DB_FILE = 'app.db'

def get_all_students():
    # 1. Establish connection to the database
    conn = sqlite3.connect(DB_FILE)
    
    # 2. Set row_factory to Row to access columns by name
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # 3. Execute the selection query
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    # 4. Convert Row objects into a standard list of dictionaries
    students = []
    for row in rows:
        students.append(dict(row))
    
    # 5. Close connection and return the data
    conn.close()
    return students

def add_student(name, group):
    # 1. Open connection
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # 2. Prepare and execute the insert command using parameterized queries
    sql = "INSERT INTO students (full_name, course_group) VALUES (?, ?)"
    values = (name, group)
    cursor.execute(sql, values)
    
    # 3. Commit changes to the database
    conn.commit()
    
    # 4. Close connection
    conn.close()