import mysql.connector

conn = mysql.connector.connect(user='user', password='password', host='host', database='database')
cursor = conn.cursor()

interest_id = 'some_value'

query = "SELECT App.url,App.leaderboard_rating,App.app_name FROM App_interest JOIN App ON App.app_id=App_interest.app_id WHERE App_interest.interest_id='{}' ORDER BY App.leaderboard_rating DESC".format(interest_id)
cursor.execute(query)

results = cursor.fetchall()
num_rows = cursor.rowcount

if num_rows != 0:
    for row in results:
        url = row[0]
        leaderboard_rating = row[1]
        app_name = row[2]

        print("<section ='app'>")
        print("<header>")
        print("<form action='../Rating/app_page.php' method='post'>")
        print("<h1>{}</h1>".format(app_name))
        print("<h4>Rating:{}</h4>".format(leaderboard_rating))
        print("<input type='hidden' name='url' value='{}'>".format(url))
        print("<input type='hidden' name='name' value='{}'>".format(app_name))
        print("<input type='hidden' name='interest' value='{}'>".format(interest_id))
        print("<input class='button' type='submit' value='View More'>")
        print("</header>")
        print("</form>")
        print("</section>")
else:
    print("NO record Found")

cursor.close()
conn.close()
