import mysql.connector

# Establish connection to the database
conn = mysql.connector.connect(user='username', password='password', host='hostname', database='database_name')

# Select distinct app ids from the Rating table
query = "SELECT DISTINCT app_id FROM Rating"
cursor = conn.cursor()
cursor.execute(query)

# Get the number of rows
num_rows = cursor.rowcount

# Loop through the app ids
for app in cursor:
    app_id = app[0]
    # Select the average rating for the current app id
    query = "SELECT app_id, AVG(rating) AS rating FROM Rating WHERE app_id = %s"
    cursor.execute(query, (app_id,))
    row = cursor.fetchone()
    if row:
        lrating = row[1]
        # Update the leaderboard rating for the current app in the App table
        update_query = "UPDATE App SET leaderboard_rating = %s WHERE app_id = %s"
        cursor.execute(update_query, (lrating, app_id))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
