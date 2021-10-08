from psycopg2 import connect

from .config import db_uri


# Get data from database
def data_from_db():
    conn = connect(db_uri)
    cursor = conn.cursor()

    # select query
    cursor.execute('select * from users_0;')

    return list(zip([i[0] for i in cursor.fetchall()]))

# Insert data to database synchronously
def sync_db_ops() -> None:
    conn = connect(db_uri)
    cursor = conn.cursor()

    data = data_from_db()
    print(len(data), "row selected")

    # Insert into the tables
    cursor.executemany("INSERT INTO users_0 (name) VALUES (%s)", data)
    cursor.executemany("INSERT INTO users_1 (name) VALUES (%s)", data)
    conn.commit()

    # Close connection
    conn.close()