from django.urls import path
from . import views

urlpatterns = [
    path('', views.pjcreation01, name="PJCreation01"),
    path('', views.pjcreation01create, name="PJCreation01Create"),
    path('', views.pjcreation02, name="PJCreation02"),
]