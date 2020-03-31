from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='website-home'),
    path('search/', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
]


# http://127.0.0.1:8000/search/?q=sorona
