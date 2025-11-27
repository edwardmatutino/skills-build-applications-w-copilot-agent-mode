
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TeamAPITests(APITestCase):
	def test_list_teams(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
