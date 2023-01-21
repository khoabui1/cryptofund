from django.db import models


# Create your models here.
class Fundraising(models.Model):
    wallet = models.CharField(max_length=65)
    firstName = models.CharField(max_length=65)
    lastName = models.CharField(max_length=65)
    description = models.TextField
    email = models.EmailField
    image = models.ImageField
    approved = models.BooleanField(default=True)


class User(models.Model):
    firstName = models.CharField(max_length=65)
    lastName = models.CharField(max_length=65)
    email = models.EmailField
    number = models.IntegerField

