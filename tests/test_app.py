"""
Unit test for app.py.
"""
import unittest
from unittest.mock import patch, MagicMock
from io import BytesIO
from app.app import RequestHandler

class TestApp(unittest.TestCase):
    """
    Unit tests for the HTTP request handler.
    """
    
    @patch('database.models.PropertyModel.get_properties')
    def test_get_properties(self, mock_get_properties):
        """
        Tests the GET properties handler by mocking the PropertyModel's get_properties method.
        """
        mock_get_properties.return_value = [
            {
                'address': 'calle 23 #45-67',
                'city': 'bogota',
                'price': 120000000,
                'description': 'Hermoso apartamento en el centro',
                'year': 2000,
                'status': 'en_venta'
            }
        ]
        
        class TestRequestHandler(RequestHandler):
            def __init__(self, request, client_address, server):
                self.request = request
                self.client_address = client_address
                self.server = server
                self.setup()
            
            def setup(self):
                self.requestline = ''
                self.command = ''
                self.request_version = ''
                self.close_connection = True

            def finish(self):
                pass

        request = MagicMock()
        client_address = ('127.0.0.1', 8080)
        server = MagicMock()

        handler = TestRequestHandler(request, client_address, server)
        
        handler.rfile = BytesIO()
        handler.wfile = BytesIO()
        handler.headers = {}

        handler.handle_get_properties({'city': ['bogota']})

        # Get the response body by stripping off the headers
        response = handler.wfile.getvalue().decode()
        body = response.split('\r\n\r\n', 1)[1]  # Splits the response into headers and body, and takes the body

        self.assertEqual(
            body,
            '[{"address": "calle 23 #45-67", "city": "bogota", "price": 120000000, "description": "Hermoso apartamento en el centro", "year": 2000, "status": "en_venta"}]'
        )

if __name__ == '__main__':
    unittest.main()
