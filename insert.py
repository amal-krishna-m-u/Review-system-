import mysql.connector

def insert_interest(conn, ui, il):
    cursor = conn.cursor()
    status_interest = "Inserted succesfully"
    for interest_item in il:
        sql = "INSERT INTO User_Interest (interest_id, user_id) VALUES (%s, %s)"
        values = (interest_item, ui)
        result = cursor.execute(sql, values)
        if not result:
            status_interest = "Not Inserted succesfully"
            break
    return status_interest

# Example usage
conn = mysql.connector.connect(host="localhost", user="root", password="", database="project")
ui = 1234
il = [1, 2, 3, 4]
status_interest = insert_interest(conn, ui, il)
if status_interest == "Inserted succesfully":
    print("Interest Added sucessfully!!!")
else:
    print("Interest Not inserted")
conn.close()
