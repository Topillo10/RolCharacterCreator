from django.urls import path
from .views import LoginView, close_session, user_login
 
urlpatterns = [
    path('', LoginView.as_view(), name="register"),
    path('close_session', close_session, name="close_session"),
    path('login', user_login, name="login"),
]