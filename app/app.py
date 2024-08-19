"""
Handles HTTP requests and defines the controllers for the endpoints.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from database.database import Database
from database.models import PropertyModel


class RequestHandler(BaseHTTPRequestHandler):
    """
    HTTP request handler that processes GET and POST requests.
    It provides endpoints to retrieve property data based on filters.
    """
    db = Database()

    def _set_response(self, status_code: int = 200) -> None:
        """
        Sets the HTTP response headers and status code.
        """
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self) -> None:
        """
        Handles GET requests to retrieve property data based on query parameters.
        """
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/properties':
            query_params = parse_qs(parsed_path.query)
            self.handle_get_properties(query_params)
        else:
            self._set_response(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode('utf-8'))

    def handle_get_properties(self, query_params: dict) -> None:
        """
        Processes the properties retrieval based on provided filters.
        """
        filters = {
            'city': query_params.get('city', [None])[0],
            'year_built': query_params.get('year_built', [None])[0],
            'status': query_params.get('status', [None])[0],
        }
        properties = PropertyModel.get_properties(self.db, filters)
        self._set_response(200)
        self.wfile.write(json.dumps(properties).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=RequestHandler, port: int = 8000) -> None:
    """
    Initializes and starts the HTTP server.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()
