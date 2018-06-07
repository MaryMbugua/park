from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Guard(models.Model):
    name =  models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    occupants_count = models.PositiveIntegerField(default=0)
    



