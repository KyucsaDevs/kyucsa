#importing path from urls and views from the the current directory respectively
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('technologies', views.technologies, name='technologies'),
    path('events', views.events, name='events'),
    path('team', views.team, name='team'),
    path('gallery', views.gallery, name='gallery'),
    path('verification', views.verify, name='verify'),
    path('membership', views.membership, name='signup'),
]