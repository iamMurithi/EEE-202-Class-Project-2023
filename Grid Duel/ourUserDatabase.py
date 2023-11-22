# This file/module handles the database logic for user authentication and game score tracking
# #How we made our database
# ourDB = sqlite3.connect('credentials.db')
# #creating a table to store a table
# a_cursor = ourDB.cursor()
# #a_cursor.execute("""
#              CREATE TABLE users(
#                  name text, password text
#                  )
#              """)
# The table, "Users" with 2 Columns: Name text, Password text
# Name Column stores User name while Password Column stores User log in Password
# #to execute the cursor command commit the connection
# ourDB.commit()
# #finally, close the connection
# ourDB.close()
import sqlite3
#Connect to our database
ourDB = sqlite3.connect('UserDatabase.db')
#Our cursor
a_cursor = ourDB.cursor()

#function to add records to our database
def add_data(name, password):
    a_cursor.execute('''INSERT INTO users (name, password) VALUES (?, ?)''', (name, password))
    ourDB.commit()
#function to query our database for the presence of a record of a user
def query_database(name, password):
    a_cursor.execute('''SELECT * FROM users WHERE name = ? AND password = ?''', (name, password))
    result = a_cursor.fetchone()
    if result is not None:
        return True
    else:
        return False
#function to close our databse connection
def close_database_connection():
    ourDB.close()
    return
#function to remove records from our database
def remove_data(name):
    a_cursor.execute('''DELETE FROM users WHERE name = ?''', (name,))
    ourDB.commit()
