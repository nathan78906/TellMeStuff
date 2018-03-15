from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dialogflow/', views.dialogflow, name='dialogflow'),
]
