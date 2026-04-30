import mysql.connector
from db_config import get_db_connection


db = mysql.connector.connect()
cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
cursor.close()
db.close()
