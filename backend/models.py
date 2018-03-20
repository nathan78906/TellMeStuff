from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weather(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    location = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

class Subreddit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    subreddit = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone_number = models.CharField(max_length=50, default=None, null=True)
    facebook_id = models.CharField(max_length=100, default=None, null=True)
    google_assistant_id = models.CharField(max_length=100, default=None, null=True)
    slack_id = models.CharField(max_length=100, default=None, null=True)
    twitter_id = models.CharField(max_length=100, default=None, null=True)
        
