from django.db import models


class Harvest(models.Model):
    name = models.CharField(max_length=200)
    date_start = models.DateField('date started')
    date_end = models.DateField('date ended')

    def __str__(self):
        return self.name
