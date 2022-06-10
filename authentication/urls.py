from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_team, name="login"),
    path('logout', views.logout_team, name="logout"),
]
