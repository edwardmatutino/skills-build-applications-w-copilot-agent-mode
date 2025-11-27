
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class APIRootTests(APITestCase):
	def test_api_root(self):
		url = reverse('api_root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn('users', response.data)
		self.assertIn('teams', response.data)
		self.assertIn('activities', response.data)
		self.assertIn('leaderboard', response.data)
