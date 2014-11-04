from django.conf.urls import patterns, include, url
from gameone import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Warzone.views.home', name='home'),
    
    url(r'^roundone/', views.roundone , name='roundone'),
)