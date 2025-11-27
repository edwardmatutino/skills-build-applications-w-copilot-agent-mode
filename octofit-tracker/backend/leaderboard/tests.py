
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class LeaderboardAPITests(APITestCase):
	def test_list_leaderboard(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
