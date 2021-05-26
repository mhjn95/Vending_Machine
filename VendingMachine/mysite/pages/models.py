from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Item(models.Model):
    machine_no = models.IntegerField(default=1,null=False)
    coke = models.IntegerField(default=10)
    pepsi = models.IntegerField(default=10)
    soda = models.IntegerField(default=10)
    one = models.IntegerField(default=5)
    five = models.IntegerField(default=5)
    ten = models.IntegerField(default=5)
    twentyfive = models.IntegerField(default=5)
    namemach = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.namemach
