
from django.db import models
from accounts.models import User

class Leaderboard(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
	points = models.IntegerField()

	def __str__(self):
		return f"{self.user.name}: {self.points}"
