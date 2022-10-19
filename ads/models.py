from django.db import models

class Ad(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
