from django.urls import path

from credentials.models import Credential
from . import views
from .views import CredentialDetailView, CredentialEditView, CredentialView, CredentialEditView
urlpatterns = [
    #path('', views.home, name="home")
    path('', CredentialView.as_view(), name="cred"),
    path('cred/<int:pk>', CredentialDetailView.as_view(), name="cred-detail"),
    path('creds/edit/<int:pk>', CredentialEditView.as_view(), name="cred-edit"),
]
