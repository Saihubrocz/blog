from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    confirmpassword = models.CharField(max_length = 100)
