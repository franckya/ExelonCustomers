from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB', 'exelon_db'),
        user=os.getenv('POSTGRES_USER', 'exelon_user'),
        password=os.getenv('POSTGRES_PASSWORD', 'securepassword'),
        host=os.getenv('POSTGRES_HOST', 'localhost'),
        port='5432'
    )
    return conn

@app.route('/')
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Hello, {os.getenv('NAME', 'World')}! Database version: {db_version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
