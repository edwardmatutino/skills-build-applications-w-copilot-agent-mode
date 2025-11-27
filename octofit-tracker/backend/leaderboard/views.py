
from rest_framework import viewsets
from .models import Leaderboard
from .serializers import LeaderboardSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer
