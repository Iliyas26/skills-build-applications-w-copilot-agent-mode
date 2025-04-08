from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class OctofitTrackerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration="00:30:00")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)
        self.workout = Workout.objects.create(name="Morning Run", description="A quick morning run.")

    def test_user_creation(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_creation(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_creation(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_creation(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workout_creation(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
