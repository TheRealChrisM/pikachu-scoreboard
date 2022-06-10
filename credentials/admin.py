from django.contrib import admin

# Register your models here.
from .models import Credential, Team

admin.site.register(Team)
admin.site.register(Credential)