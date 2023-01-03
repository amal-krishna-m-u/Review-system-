from django.db import connections

def my_view(request):
    # Get connection
    conn = connections['default']

    # Run query
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM my_table")
        rows = cursor.fetchall()

    return render(request, 'my_template.html', {'rows': rows})
