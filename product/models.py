from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=63)
    slug = models.SlugField(max_length=31,unique=True)
    logo = models.CharField(max_length=31)

class Type(models.Model):
    name = models.CharField(max_length=63)

class Product(models.Model):
    name = models.CharField(max_length=63)
    model = models.CharField(max_length=40,unique=True)
    decription = models.CharField(max_length=500)
    extra_info = models.CharField(max_length=63)
    slug = models.CharField(max_length=31,unique=True)
    pic = models.CharField(max_length=31)
    date_released = models.DateField('date released',auto_now_add=True)
    price = models.IntegerField()
    discount_percentage = models.FloatField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    type_of_product = models.ForeignKey(Type,on_delete=models.CASCADE)


