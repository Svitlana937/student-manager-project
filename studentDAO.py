from db_config import get_db_connection

def get_all_students():
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT * FROM student"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def get_student_by_id(student_id):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT * FROM student WHERE id = %s"
    values = (student_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result