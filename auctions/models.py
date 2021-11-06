from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related, AutoField
from django.conf import settings


class User(AbstractUser):
    pass

class Listings(models.Model):
    user = models.CharField(max_length=200, default=None)
    listing = models.CharField(max_length=64)
    description = models.TextField()
    ini_bid = models.IntegerField()
    url = models.URLField(max_length=200, default=None)
    category = models.CharField(max_length=64, default=None)
    Active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.listing}"

class Bids(models.Model):
    item = models.ForeignKey(Listings,default= 1,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    bid = models.CharField(max_length=64,blank=True)

    def __str__(self):
        return f"{self.bid}: {self.user}"

class Comments(models.Model):
    item = models.ForeignKey(Listings,default= 1, on_delete=CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user}: {self.comment}"        

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(Listings)

    def __str__(self):
        return f"{self.user}:{self.item}"

