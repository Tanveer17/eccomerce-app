from django.db import models

from user.models import User
from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField()

