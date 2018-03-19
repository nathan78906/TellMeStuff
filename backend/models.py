from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weather(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    location = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone_number = models.CharField(max_length=50, default=None)
    facebook_id = models.CharField(max_length=100, default=None)
    google_assistant_id = models.CharField(max_length=100, default=None)
    slack_id = models.CharField(max_length=100, default=None)
    twitter_id = models.CharField(max_length=100, default=None)
        
