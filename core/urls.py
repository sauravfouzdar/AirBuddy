from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^a/submit/$', views.main_submit, name='main_submit'),
    
]