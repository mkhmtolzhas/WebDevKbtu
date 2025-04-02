from django.db import models

class Book(models.Model):
    price = models.FloatField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
