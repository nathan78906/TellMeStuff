from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt   

from . import views

urlpatterns = [
    url(r'^dialogflow/', csrf_exempt(views.dialogflow), name='dialogflow'),
]
