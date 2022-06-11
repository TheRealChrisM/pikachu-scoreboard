from msilib.schema import ServiceControl
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.
class Team(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    members = models.CharField(max_length=300)
    contact = models.EmailField()


class Credential(models.Model):
    teamnid = models.IntegerField()
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    port = models.IntegerField() 
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('cred-detail', args=(str(self.id)))
