
from django.db import models
from accounts.models import User

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	type = models.CharField(max_length=50)
	duration = models.IntegerField()  # duration in minutes

	def __str__(self):
		return f"{self.user.name} - {self.type}"
