from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt   

from . import views

urlpatterns = [
    url(r'^dialogflow/', views.dialogflow, name='dialogflow'),
]
