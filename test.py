import pyodbc

# Database connection parameters
SERVER = r'DESKTOP-0JQ7NM2\SQLEXPRESS'
DATABASE = 'dbpyapp'
USERNAME = ''  # No username needed for Windows Authentication
PASSWORD = ''  # No password needed for Windows Authentication
DRIVER = '{ODBC Driver 17 for SQL Server}'
TIMEOUT = 1
TRUSTED_CONNECTION = 'YES'

# Create a connection string
connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};TRUSTED_CONNECTION={TRUSTED_CONNECTION}'

# Test the connection
try:
    connection = pyodbc.connect(connection_string, timeout=TIMEOUT)
    print("Connection successful!")
    
    # Test by running a simple query
    cursor = connection.cursor()
    cursor.execute("SELECT TOP 5 * FROM categories")
    
    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    connection.close()

except Exception as e:
    print("Error: Could not connect to the database")
    print(str(e))
