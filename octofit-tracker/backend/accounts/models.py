
from django.db import models
from teams.models import Team

class User(models.Model):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=100)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

	def __str__(self):
		return self.name
