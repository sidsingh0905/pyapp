import os
import pyodbc


# Read environment variables from .env
SERVER = os.getenv('DB_SERVER', 'sql_server')  # Use sql_server as the container name
DATABASE = os.getenv('DB_NAME', 'dbpyapp')  # Database name
USERNAME = os.getenv('DB_USERNAME', 'sa')  # Default SQL Server admin username
PASSWORD = os.getenv('DB_PASSWORD', 'Siddhant@9')  # Password for the 'sa' user
DRIVER = os.getenv('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')
TIMEOUT = 5  # Timeout to avoid hanging queries
TRUSTED_CONNECTION = os.getenv('DB_TRUSTED_CONNECTION', 'NO')

# Example of a connection string
conn = pyodbc.connect(f'DRIVER={{{DRIVER}}};'
                      f'SERVER={SERVER},1433;'  # 1433 is the default port for SQL Server
                      f'DATABASE={DATABASE};'
                      f'UID={USERNAME};'  # Use the sa username
                      f'PWD={PASSWORD}')  # Use the sa password
