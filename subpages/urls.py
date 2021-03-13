from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^a/memes/$', views.memes_main, name='memes_main'),
    url(r'^a/memes/submit$', views.memes_create, name='memes_create'),

    url(r'^a/confessions/$', views.confessions_main, name='confessions_main'),
    url(r'^a/confessions/(?P<pk>\d+)/$', views.confession_body, name='confession_body'),
    url(r'^a/confessions/submit$', views.confession_create, name='confession_create'),
    
]