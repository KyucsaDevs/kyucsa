#importing path from urls and views from the the current directory respectively
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('technologies', views.technologies, name='technologies'),
    path('workshops', views.workshops, name='workshops'),
    path('team', views.team, name='team'),
    path('gallery', views.gallery, name='gallery'),
    path('live_events', views.live_events, name='live'),
    path('upcomingevnts', views.upcomingevents, name='upcomingevents'),
    path('pastevents', views.pastevents, name='pastevents'),
    path('verification', views.verify, name='verify'),
    path('membership', views.membership, name='signup'),
]