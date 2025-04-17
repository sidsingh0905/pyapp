# Set up the database connection
# SERVER = 'DESKTOP-0JQ7NM2\SQLEXPRESS'
# DATABASE = 'dbpyapp'
# USERNAME = 'PYAPP_USER' 
# PASSWORD = 'Siddhant@9'
# DRIVER = '{ODBC Driver 17 for SQL SERVER}'
# TIMEOUT = 1 # Setting Timeout to 1 second
# TRUSTED_CONNECTION = 'YES'

# SERVER = 'sql_server'  # The name of the SQL Server container in Docker Compose
# DATABASE = 'dbpyapp'
# USERNAME = 'sa'  # Default SQL Server admin username
# PASSWORD = 'Siddhant@9'  # The password you set for the SQL Server instance
# DRIVER = '{ODBC Driver 17 for SQL Server}'
# TIMEOUT = 5  # Timeout to avoid hanging queries
# TRUSTED_CONNECTION = 'NO'

# sample_config.py

# # The name of the SQL Server container in Docker Compose
# SERVER = 'sql_server'

# # The database name to connect to
# DATABASE = 'dbpyapp'

# # Default SQL Server admin username
# USERNAME = 'sa'

# # The password you set for the SQL Server instance
# PASSWORD = 'Siddhant@9'

# # ODBC driver for SQL Server
# DRIVER = '{ODBC Driver 17 for SQL Server}'

# # Timeout to avoid hanging queries
# TIMEOUT = 5

# # Whether to use a trusted (Windows) connection
# TRUSTED_CONNECTION = 'NO'


import os

# Pull from environment variables with safe fallbacks
SERVER = os.getenv("DB_SERVER", "sql_server")
DATABASE = os.getenv("DB_NAME", "dbpyapp")
USERNAME = os.getenv("DB_USERNAME", "sa")
PASSWORD = os.getenv("DB_PASSWORD", "Siddhant@9")
DRIVER = os.getenv("DB_DRIVER", "{ODBC Driver 17 for SQL Server}")
TRUSTED_CONNECTION = os.getenv("DB_TRUSTED_CONNECTION", "NO")
TIMEOUT = 5

# Optional: Debug print (only during development)
print("  Loaded DB config:")
print(f"SERVER = {SERVER}")
print(f"DATABASE = {DATABASE}")
print(f"USERNAME = {USERNAME}")
print(f"PASSWORD = {PASSWORD}")
print(f"DRIVER = {DRIVER}")
print(f"TRUSTED_CONNECTION = {TRUSTED_CONNECTION}")
