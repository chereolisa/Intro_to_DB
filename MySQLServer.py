import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',        # Change if your MySQL host is different
            user='your_username',    # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection if they are open
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()