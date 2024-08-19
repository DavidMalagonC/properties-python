"""
Manage the connection and queries to the MySQL database.
"""

import mysql.connector
from mysql.connector import Error
from config.config import Config


class Database:
    """
    Manages the connection to the MySQL database
    and provides methods to execute SQL queries.
    """
    def __init__(self):
        """
        Initializes the database connection using credentials from the Config class.
        """
        try:
            self.conn = mysql.connector.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_SCHEMA
            )
            if self.conn.is_connected():
                print("Connected to MySQL database")

        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            self.conn = None

    def execute_query(self, query: str, params: list = None) -> list:
        """
        Executes a SELECT SQL query and returns the result as a list of dictionaries.
        """
        if self.conn is None:
            raise ConnectionError("Not connected to the database")

        with self.conn.cursor(dictionary=True) as cur:
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            return cur.fetchall()

    def close(self) -> None:
        """
        Closes the database connection if it is active.
        """
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Database connection closed")
