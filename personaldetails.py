# Import the MySQL connector for Python
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='hostname',
    user='username',
    password='password',
    database='database_name'
)

# Create a cursor to execute queries
cursor = conn.cursor()

# Execute the SELECT query to fetch user details
sql = "SELECT * FROM User_details WHERE user_id=%s"
cursor.execute(sql, (user_id,))

# Fetch the result set
details = cursor.fetchone()

# Print the user details
print(f"User Name: {details['user_name']}")
print(f"User E-mail: {details['email']}")
print(f"User's DOB: {details['dob']}")
