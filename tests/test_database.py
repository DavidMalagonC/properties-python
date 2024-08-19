"""
Unit test for database.py.
"""

import unittest
from database.database import Database


class TestDatabase(unittest.TestCase):
    """
    Unit tests for the Database class.
    """
    def setUp(self):
        """
        Sets up a new Database instance before each test.
        """
        self.db = Database()

    def test_execute_query(self):
        """
        Tests that the execute_query method returns a result when querying the database.
        """
        result = self.db.execute_query('SELECT DATABASE()')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
