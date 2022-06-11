from django.shortcuts import render

from services.models import Service
from django.views.generic import ListView

# Create your views here.
class ServiceView(ListView):
    model = Service
    template_name = 'services.html'