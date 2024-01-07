from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images1 = models.ImageField(upload_to='midea/img/home/')
    title = models.CharField(max_length=80)
    images2 = models.ImageField(upload_to='midea/img/home/')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Listing_Picture(models.Model):
    images = models.ImageField(upload_to='midea/img/listing_picture/')


class Lost_Information(models.Model):
    category = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    datelost = models.DateField()
    subcategory = models.CharField(max_length=60)
    brand = models.CharField(max_length=40)
    primary_color = models.CharField(max_length=60)
    Secondary_color = models.CharField(max_length=60)
    description = models.TextField()
    location = models.TextField()
