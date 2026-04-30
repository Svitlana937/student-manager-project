import mysql.connector
from db_config import get_db_connection

db = mysql.connector.connect()
cursor = db.cursor()
sql="select * from student where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
 print(x)
cursor.close()
db.close()