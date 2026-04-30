import mysql.connector
from db_config import get_db_connection

db = mysql.connector.connect()
cursor = db.cursor()
sql="delete from student where id = %s"
values = (1,)
cursor.execute(sql, values)
db.commit()
print("delete done")
cursor.close()
db.close()