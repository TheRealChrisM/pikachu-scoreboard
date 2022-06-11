from django.db import models
from django.forms import CharField
# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    team_id = models.IntegerField()
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
