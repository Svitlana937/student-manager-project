# Import necessary modules and functions
from db_config import get_db_connection
import mysql.connector


# Data Access Object (DAO) for Student
def get_all_students():
    db = get_db_connection() # Establish a new database connection
    cursor = db.cursor(dictionary=True) # Create a cursor that returns results as dictionaries
    sql = "SELECT * FROM student" # SQL query to select all students
    cursor.execute(sql) # Execute the SQL query
    result = cursor.fetchall() # Fetch all results from the executed query
    cursor.close()
    db.close()
    return result

# User authentication function
def check_user(username, password):
    if username == "root" and password == "pass":
        return {"name": "root"}
    return None
    
 
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return user

# Get student by ID
def get_student_by_id(student_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM student WHERE id = %s"
    values = (student_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def add_student(name, age):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "INSERT INTO student (name, age) VALUES (%s, %s)"
    values = (name, age)
    cursor.execute(sql, values)
    db.commit()
    last_id = cursor.lastrowid
    cursor.close()
    db.close()
    return last_id

def delete_student(student_id):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "DELETE FROM student WHERE id = %s"
    values = (student_id,)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()

def update_student(student_id, name, age):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "UPDATE student SET name = %s, age = %s WHERE id = %s"
    values = (name, age, student_id)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()