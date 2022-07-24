from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vehicles_id = models.IntegerField(
        primary_key=True, null=False, unique=True)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    direction = models.CharField(max_length=20)
    speed = models.FloatField()
