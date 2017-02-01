from django.db import models

from safra.models import Harvest, Product


class Service(models.Model):
    name = models.CharField(max_length=200)
    date_start = models.DateField('date started')
    date_end = models.DateField('date ended')
    harvest = models.ForeignKey(Harvest)
    products = models.ManyToManyField(Product, through='UsedProducts')
    cost = models.FloatField(default=0)

    def __str__(self):
        return self.name


class UsedProducts(models.Model):
    product = models.ForeignKey(Product)
    service = models.ForeignKey(Service)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
