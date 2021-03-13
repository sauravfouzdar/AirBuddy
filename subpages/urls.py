from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^a/memes/$', views.memes_main, name='memes_main'),
    url(r'^a/memes/submit$', views.memes_create, name='memes_create'),
    
]