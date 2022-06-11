from django.urls import path

from credentials.models import Credential
from . import views
from .views import ServiceView
urlpatterns = [
    #path('', views.home, name="home")
    path('', ServiceView.as_view(), name="services"),
]
