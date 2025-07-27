import psycopg2
from psycopg2.extras import DictCursor

db_config = {
    'host': 'localhost',
    'port': '5432',
    'user': 'home3',
    'password': 'home3',
    'database': 'home3',
}

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor(cursor_factory=DictCursor)

    query = "select * from staff"
    cursor.execute(query)
    result = cursor.fetchall()

    for staff in result:
        print(dict(staff))
    conn.close()
except Exception as e:
    print(e)
