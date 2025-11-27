
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from teams.models import Team
from activities.models import Activity
from leaderboard.models import Leaderboard
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='Running', duration=30),
            Activity.objects.create(user=users[1], type='Cycling', duration=45),
            Activity.objects.create(user=users[2], type='Swimming', duration=60),
            Activity.objects.create(user=users[3], type='Yoga', duration=20),
        ]

        # Create leaderboard entries
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=80)
        Leaderboard.objects.create(user=users[2], points=120)
        Leaderboard.objects.create(user=users[3], points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

        # Ensure unique index on email for users collection using pymongo
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        db.users.create_index([('email', 1)], unique=True)
