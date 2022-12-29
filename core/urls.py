from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('team/', views.team, name="team"),
    path('speakers/', views.speakers, name="speakers"),

    # redirect urls
    path('', views.redir, name="redir"),
    path('Home/', views.redir, name="redir"),
]
