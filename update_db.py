import mysql.connector
from db_config import get_db_connection

db = mysql.connector.connect()
cursor = db.cursor()
sql="update student set name= %s, age=%s where id = %s"
values = ("Joe",33, 1)
cursor.execute(sql, values)
db.commit()
print("update done")
cursor.close()
db.close()
