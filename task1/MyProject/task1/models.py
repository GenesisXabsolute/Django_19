from django.db import models

class Buyers(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=6)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=100, decimal_places=6)
    size = models.DecimalField(max_digits=100, decimal_places=6)
    description = models.TextField()
    age_limited = models.BooleanField(db_default=False)
    buyers = models.ManyToManyField(Buyers)
    