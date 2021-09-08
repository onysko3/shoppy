from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    price = models.CharField(max_length=10)
    location = models.CharField(max_length=300)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PictureItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures/')
