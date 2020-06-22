from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField()
    password = models.CharField(max_length=30)


