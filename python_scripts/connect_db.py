"""
Creates a base dataframe out of churn_modelling table and creates 3 separate dataframes out of it.
"""
import psycopg2

# postgres_host = os.environ.get('postgres_host')
# postgres_database = os.environ.get('postgres_database')
# postgres_user = os.environ.get('postgres_user')
# postgres_password = os.environ.get('postgres_password')
# postgres_port = os.environ.get('postgres_port')

postgres_host = 'localhost'
postgres_database = 'mydatabase'
postgres_user = 'myuser'
postgres_password = 'mypassword'
postgres_port = 5432

try:
    conn = psycopg2.connect(
        host=postgres_host,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password,
        port=postgres_port
    )
    cur = conn.cursor()
    print('Postgres server connection is successful')
except Exception as e:
    print("Couldn't create the Postgres connection")


def create_table():
    try:
        command = """
        CREATE TABLE IF NOT EXISTS tips (
        id SERIAL PRIMARY KEY,
        total_bill NUMERIC,
        tip NUMERIC,
        sex VARCHAR(10),
        smoker VARCHAR(3),
        day VARCHAR(10),
        time VARCHAR(10),
        size INTEGER
    )
    """
        cur.execute(command)
        conn.commit()
        print('Table created successfully')
    except Exception as e:
        print('Table creation failed')  


def insert_data(id, total_bill, tip, sex, smoker, day, time, size):
    try:
        command = """
        INSERT INTO tips(id, total_bill, tip, sex, smoker, day, time, size) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(command, (id, total_bill, tip, sex, smoker, day, time, size))
        conn.commit()
        print('Data inserted successfully')
        
    except Exception as e:
        print(e)
        print('Data insertion failed: ')


# insert_data(3, 100, 2.8, 'male', 'no', 'sun', 'dinner', 5)
