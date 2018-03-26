from django.contrib import admin
from .models import Weather, Profile, Subreddit, Motivation, UrbanDictionary

# Register your models here.
admin.site.register(Weather)
admin.site.register(Profile)
admin.site.register(Motivation)
admin.site.register(Subreddit)
admin.site.register(UrbanDictionary)
