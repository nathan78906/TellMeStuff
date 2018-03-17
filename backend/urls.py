from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^api/dialogflow/', views.dialogflow, name='dialogflow'),
]
