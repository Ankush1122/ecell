from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('home/', views.home, name="home"),
    path('team/', views.team, name="team"),
    # redirect urls
    path('', views.redir, name="redir"),
    path('Home/', views.redir, name="redir"),
]
