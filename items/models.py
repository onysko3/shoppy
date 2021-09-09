import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse
from .validators import validate_price


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    price = models.CharField(max_length=10, validators=[validate_price])
    location = models.CharField(max_length=300)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    picture = models.ImageField(upload_to='pictures/', default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('items:detail', args=[str(self.id)])
