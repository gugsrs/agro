from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    avg_price = models.FloatField(default=0)

    def __str__(self):
        return self.name
