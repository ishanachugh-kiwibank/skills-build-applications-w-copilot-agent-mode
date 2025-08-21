from django.core.management.base import BaseCommand
from djongo import models
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Create unique index for email in users
        db.users.create_index({'email': 1}, unique=True)

        # Sample data
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'dc'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'dc'},
        ]
        teams = [
            {'name': 'marvel', 'members': ['ironman@marvel.com', 'cap@marvel.com']},
            {'name': 'dc', 'members': ['batman@dc.com', 'wonderwoman@dc.com']},
        ]
        activities = [
            {'user': 'ironman@marvel.com', 'activity': 'run', 'distance': 5},
            {'user': 'batman@dc.com', 'activity': 'cycle', 'distance': 10},
        ]
        leaderboard = [
            {'team': 'marvel', 'points': 100},
            {'team': 'dc', 'points': 90},
        ]
        workouts = [
            {'user': 'cap@marvel.com', 'workout': 'pushups', 'count': 50},
            {'user': 'wonderwoman@dc.com', 'workout': 'squats', 'count': 60},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
