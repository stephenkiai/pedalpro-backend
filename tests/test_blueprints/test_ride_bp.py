import unittest
from flask import Flask, jsonify
from models import db, Ride, RideParticipants
from app import app

class TestRideBlueprint(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_ride(self):
        response = self.app.post(
            '/ride/create',
            json={"name": "Test Ride", "location": "Test Location", "distance": "10 miles", "start_datetime": "01/01/2023 12:00:00"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("ride_id", response.json)

    def test_join_ride(self):
        # Assuming you have a registered user and a created ride for testing
        user_response = self.app.post(
            '/user/register',
            json={"name": "testuser", "email": "test@example.com", "password": "testpassword", "role": "user"}
        )

        ride_response = self.app.post(
            '/ride/create',
            json={"name": "Test Ride", "location": "Test Location", "distance": "10 miles", "start_datetime": "01/01/2023 12:00:00"}
        )

        response = self.app.post(
            f'/ride/join/{ride_response.json["ride_id"]}',
            json={"user_id": user_response.json["user_id"]}
        )
        self.assertEqual(response.status_code, 200)

    def test_all_rides(self):
        
        self.app.post(
            '/ride/create',
            json={"name": "Ride 1", "location": "Location 1", "distance": "5 miles", "start_datetime": "01/01/2023 10:00:00"}
        )
        self.app.post(
            '/ride/create',
            json={"name": "Ride 2", "location": "Location 2", "distance": "8 miles", "start_datetime": "01/02/2023 15:00:00"}
        )

        response = self.app.get('/ride/all')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    

if __name__ == '__main__':
    unittest.main()
