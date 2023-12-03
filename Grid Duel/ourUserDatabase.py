# Import the SQLite module
import sqlite3

# Connect to our database
ourDB = sqlite3.connect('UserDatabase.db')

# Initialize a cursor for database operations
a_cursor = ourDB.cursor()

# Function to add records to our database
def add_data(name, password):
    # Execute an SQL command to insert data into the 'users' table
    a_cursor.execute('''INSERT INTO users (name, password) VALUES (?, ?)''', (name, password))
    # Commit the changes to the database
    ourDB.commit()

# Function to query the database for the presence of a user record
def query_database(name, password):
    # Execute an SQL command to select data from the 'users' table based on name and password
    a_cursor.execute('''SELECT * FROM users WHERE name = ? AND password = ?''', (name, password))
    # Fetch one result
    result = a_cursor.fetchone()
    # Check if a record was found
    if result is not None:
        return True
    else:
        return False

# Function to close the database connection
def close_database_connection():
    # Close the database connection
    ourDB.close()
    return

# Function to remove records from our database
def remove_data(name):
    # Execute an SQL command to delete data from the 'users' table based on name
    a_cursor.execute('''DELETE FROM users WHERE name = ?''', (name,))
    # Commit the changes to the database
    ourDB.commit()
