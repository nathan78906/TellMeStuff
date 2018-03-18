from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^api/signup/', views.api_signup, name='api_signup'),
    url(r'^api/signin/', views.api_signin, name='api_signin'),
    url(r'^api/dialogflow/', views.dialogflow, name='dialogflow'),
]
