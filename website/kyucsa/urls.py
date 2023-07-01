#importing path from urls and views from the the current directory respectively
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('live', views.live, name='live'),
    path('pastevnts', views.pastevents, name='pastevents'),
    path('upcoming', views.upcomingevents, name='upcomingevents'),
    path('verification', views.verify, name='verify'),
    path('membership', views.membership, name='signup'),
]