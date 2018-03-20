from django.contrib import admin
from .models import Weather, Profile, Motivation

# Register your models here.
admin.site.register(Weather)
admin.site.register(Profile)
admin.site.register(Motivation)
