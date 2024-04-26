import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        response = self.app.get('/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Hello from the API server!')

if __name__ == '__main__':
    unittest.main()
