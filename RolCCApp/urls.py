from django.urls import path
from RolCCApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('levelup', views.levelup, name="LevelUp"),
    path('search', views.search, name="Search"),
    path('news', views.search, name="News"),
]