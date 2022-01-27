from django.db import models
from django.utils import timezone
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)

