import unittest
from flask import Flask, jsonify
from models import db, Users
from app import app

class TestUserBlueprint(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        response = self.app.post(
            '/user/register',
            json={"name": "testuser", "email": "test@example.com", "password": "testpassword", "role": "user"}
        )
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        # Assuming you have a registered user for testing
        self.app.post(
            '/user/register',
            json={"name": "testuser", "email": "test@example.com", "password": "testpassword", "role": "user"}
        )

        response = self.app.post(
            '/user/login',
            json={"login_identifier": "test@example.com", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json)

    def test_get_user_data(self):
        # Assuming you have a registered user for testing
        user_response = self.app.post(
            '/user/register',
            json={"name": "testuser", "email": "test@example.com", "password": "testpassword", "role": "user"}
        )

        access_token = self.get_access_token(user_response)

        response = self.app.get(
            '/user/user-data',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("userid", response.json)

    def test_all_users(self):
       
        self.app.post(
            '/user/register',
            json={"name": "user1", "email": "user1@example.com", "password": "password1", "role": "user"}
        )
        self.app.post(
            '/user/register',
            json={"name": "user2", "email": "user2@example.com", "password": "password2", "role": "user"}
        )

        response = self.app.get('/user/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

   

    def get_access_token(self, user_response):
        login_response = self.app.post(
            '/user/login',
            json={"login_identifier": user_response.json["email"], "password": "testpassword"}
        )
        return login_response.json.get("access_token")

if __name__ == '__main__':
    unittest.main()
