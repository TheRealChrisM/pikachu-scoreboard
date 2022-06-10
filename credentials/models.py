from msilib.schema import ServiceControl
from django.db import models

# Create your models here.
class Team(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    members = models.CharField(max_length=300)
    contact = models.EmailField()


class Credential(models.Model):
    teamnid = models.IntegerField()
    service = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

