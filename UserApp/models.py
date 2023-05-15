from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AppUser:
    email = models.CharField(max_length=254, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
