from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^a/memes/$', views.memes_main, name='memes_main'),
    url(r'^a/memes/submit$', views.memes_create, name='memes_create'),

    url(r'^a/confessions/$', views.confessions_main, name='confessions_main'),
    url(r'^a/confessions/(?P<pk>\d+)/$', views.confession_body, name='confession_body'),
    url(r'^a/confessions/submit$', views.confession_create, name='confession_create'),

    url(r'^a/ml/$', views.ml_main, name='ml_main'),
    url(r'^a/ml/(?P<pk>\d+)/$', views.ml_body, name='ml_body'),
    url(r'^a/ml/submit/$', views.ml_create, name='ml_create'),

    url(r'^a/webd/$', views.webd_main, name='webd_main'),
    url(r'^a/webd/(?P<pk>\d+)$', views.webd_body, name='webd_body'),
    url(r'^a/webd/submit/$', views.webd_create, name='webd_create'),

    url(r'^a/examCorner/$', views.examCorner_main, name='examCorner_main'),
    url(r'^a/examCorner/(?P<pk>\d+)$', views.examCorner_body, name='examCorner_body'),
    url(r'^a/examCorner/submit/$', views.examCorner_create, name='examCorner_create'),


    
]