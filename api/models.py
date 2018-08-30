from django.db import models


class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vin = models.CharField(max_length=50, null=True, blank=True)