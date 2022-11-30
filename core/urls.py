from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/', views.home, name="home"),
    # redirect urls
    path('', views.redir, name="redir"),
    path('Home/', views.redir, name="redir"),
]
