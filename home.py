import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project"
)

cursor = conn.cursor()

user_id = session['login_session']

sql = "SELECT Interest.interest_name FROM User_Interest JOIN Interest ON User_Interest.interest_id = Interest.interest_id WHERE User_Interest.user_id=%s"
cursor.execute(sql, (user_id,))

result = cursor.fetchall()

if result:
    for interest in result:
        print(f'<div class="interest">{interest["interest_name"]}</div>')
else:
    print(cursor.error())

cursor.close()
conn.close()
