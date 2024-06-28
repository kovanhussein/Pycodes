import unittest
from unittest.mock import patch
from utils.api_requests import fetch_data

class TestAPIRequests(unittest.TestCase):
    @patch('utils.api_requests.requests.get')
    def test_fetch_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"userId": 1, "id": 1, "title": "Test", "completed": False}

        data = fetch_data('https://jsonplaceholder.typicode.com/todos/1')
        self.assertEqual(data['title'], 'Test')

if __name__ == '__main__':
    unittest.main()
