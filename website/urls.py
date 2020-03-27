from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.conf.urls.defaults import *

urlpatterns = [
    path('', views.home, name='website-home'),
    path('search/', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path(r'', include('gmapi.urls.media')),
]


# http://127.0.0.1:8000/search/?q=sorona
