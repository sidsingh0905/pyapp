# # Set up the database connection
# SERVER = 'DESKTOP-0JQ7NM2\SQLEXPRESS'
# DATABASE = 'dbpyapp'
# USERNAME = 'PYAPP_USER' 
# PASSWORD = 'Siddhant@9'
# DRIVER = '{ODBC Driver 17 for SQL SERVER}'
# TIMEOUT = 1 # Setting Timeout to 1 second
# TRUSTED_CONNECTION = 'YES'

SERVER = 'sqlserver'  # The name of the SQL Server container in Docker Compose
DATABASE = 'dbpyapp'
USERNAME = 'sa'  # Default SQL Server admin username
PASSWORD = 'Siddhant@9'  # The password you set for the SQL Server instance
DRIVER = '{ODBC Driver 17 for SQL Server}'
TIMEOUT = 5  # Timeout to avoid hanging queries
TRUSTED_CONNECTION = 'NO'