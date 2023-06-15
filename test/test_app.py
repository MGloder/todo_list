import unittest
from flask import Flask
from app.routes import todos_routes


class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask application
        self.app = Flask(__name__)
        self.app.testing = True

        # Register the routes from the separate routes file
        self.app.register_blueprint(todos_routes)

        # Create a test client
        self.client = self.app.test_client()

    def test_todo_list(self):
        response = self.client.get('/todos')
        self.assertEqual(response.status_code, 200)
        # Add additional assertions for the expected response data

    def test_add_todo(self):
        response = self.client.post('/todos/add', data={'todo_item': 'Test todo'})
        self.assertEqual(response.status_code, 302)  # Assuming a redirect response
        # Add additional assertions to verify the todo was added correctly

    def test_complete_todo(self):
        response = self.client.post('/todos/complete/1')
        self.assertEqual(response.status_code, 302)
