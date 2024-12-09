from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    db_host = os.getenv('DB_HOST', 'mysql')
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', 'password')
    db_name = os.getenv('DB_NAME', 'test')

    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        return "Connected to Database!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
