from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable


create_db = "CREATE DATABASE workshop"

create_table_user = """CREATE TABLE users(
id SERIAL,
username VARCHAR(255) UNIQUE,
hashed_password VARCHAR(80)
"""

create_table_message = """CREATE TABLE message(
id SERIAL,
from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
to_id INTEGER references users(id) ON DELETE CASCADE,
creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
text VARCHAR(255)
)"""

db_user = "postgres"
db_password = "coderslab"
db_host = "127.0.0.1"
try:
    cnx = connect( database='workshop', user=db_user, password=db_password, host=db_host )
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(create_table_user)
        print("Table created successfully")
    except DuplicateDatabase as e:
        print("Table already exists", e)
    cnx.close()
except OperationalError as e:
    print("Connection error", e)