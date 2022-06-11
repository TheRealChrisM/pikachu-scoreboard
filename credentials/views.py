from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from credentials.models import Credential
from .models import Credential
# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class CredentialView(ListView):
    model = Credential
    template_name = 'credentials.html'

class CredentialDetailView(DetailView):
    model = Credential
    template_name = 'credential_detail.html'

class CredentialEditView(UpdateView):
    model = Credential
    template_name = "credential_edit.html"
    fields = ['username','password']