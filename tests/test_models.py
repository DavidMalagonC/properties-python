"""
Unit test for models.py.
"""

import unittest
from unittest.mock import Mock, patch

from database.models import PropertyModel


class TestPropertyModel(unittest.TestCase):
    """
    Unit tests for the PropertyModel class.
    """

    @patch('mysql.connector.connect')
    def test_get_properties_with_filters(self, mock_connect):
        """
        Tests the get_properties method with specific filters for city and year.
        """
        mock_db = Mock()
        mock_connect.return_value = mock_db
        mock_db.execute_query.return_value = [
            {
                'address': '123 Main St',
                'city': 'New York',
                'price': 500000,
                'description': 'Nice apartment',
                'year': 2020,
                'status': 'en_venta'
            },
            {
                'address': '456 Elm St',
                'city': 'Los Angeles',
                'price': 750000,
                'description': 'Beautiful house',
                'year': 2018,
                'status': 'pre_venta'
            },
        ]

        filters = {'city': 'New York', 'year': 2020}

        properties = PropertyModel.get_properties(mock_db, filters)

        self.assertEqual(len(properties), 2)
        self.assertEqual(properties[0]['city'], 'New York')
        self.assertEqual(properties[0]['year'], 2020)
        self.assertNotEqual(properties[1]['city'], 'New York')

    @patch('mysql.connector.connect')
    def test_get_properties_with_empty_filters(self, mock_connect):
        """
        Tests the get_properties method with no filters applied.
        """
        mock_db = Mock()
        mock_connect.return_value = mock_db
        mock_db.execute_query.return_value = [
            {
                'address': '123 Main St',
                'city': 'New York',
                'price': 500000,
                'description': 'Nice apartment',
                'year': 2020,
                'status': 'en_venta'
            },
            {
                'address': '456 Elm St',
                'city': 'Los Angeles',
                'price': 750000,
                'description': 'Beautiful house',
                'year': 2018,
                'status': 'pre_venta'
            },
        ]

        filters = {}

        properties = PropertyModel.get_properties(mock_db, filters)

        self.assertEqual(len(properties), 2)
        self.assertEqual(properties[0]['city'], 'New York')
        self.assertEqual(properties[1]['city'], 'Los Angeles')


if __name__ == '__main__':
    unittest.main()
