import psycopg2

def open_connection():
    conn = psycopg2.connect(database = "task",
                        user = "postgres",
                        host = "localhost",
                        password = "Muhammad_0010",
                        port = 5432
                        )
    return conn

def close_connection(conn, cur):
    cur.close()
    conn.close()

def create_database_tables():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        due_date DATE,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    )
"""
    )
    conn.commit()
    close_connection(conn, cursor)

