import os
import pyodbc
from flask import Flask

app = Flask(__name__)

# Retrieve the database connection details from environment variables
server = os.getenv('DB_HOST', 'sql_server')  # Default is 'sql_server' (the service name in docker-compose.yml)
port = os.getenv('DB_PORT', '1433')          # Default SQL Server port
database = os.getenv('DB_NAME', 'dbpyapp')   # The database name
username = os.getenv('DB_USER', 'sa')        # Default SQL Server user
password = os.getenv('DB_PASSWORD', 'YourStrong!Passw0rd')  # Default password

# Connection string for SQL Server
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'

@app.route('/')
def test_connection():
    try:
        # Trying to connect to the SQL Server
        conn = pyodbc.connect(conn_str)
        return "Connection successful!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
