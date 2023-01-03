# Importing necessary libraries
import mysql.connector
from mysql.connector import Error
import os
from flask import Flask, render_template, request, redirect, session

# Initializing Flask app
app = Flask(__name__)

# Establishing connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='project',
        user='root',
        password=''
    )
    cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

# Starting the session
session_start()

# Storing the user_id from the session
ui = session['login_session']

# Selecting all data from the User_details table where the user_id matches the logged in user's id
sql = "SELECT * FROM User_details WHERE user_id='{}'".format(ui)
cursor.execute(sql)

# Storing the result of the query
result = cursor.fetchone()

# If the result exists, store the row in the variable 'row'
if result:
    row = result

# If there is an error, print an error message
else:
    print("Error: {}".format(cursor.error))

# Selecting the count and sum of the ratings where the user_id matches the logged in user's id
sql1 = "SELECT COUNT(*) AS count FROM Rating WHERE user_id='{}'".format(ui)
sql2 = "SELECT SUM(rating) AS sum FROM Rating WHERE user_id='{}'".format(ui)
cursor.execute(sql1)
cursor.execute(sql2)

# Storing the count and sum results in the variables 'count' and 'sum'
count = cursor.fetchone()
sum = cursor.fetchone()

# Rendering the template with the data from the database
return render_template('dashboard.html', row=row, count=count, sum=sum)
