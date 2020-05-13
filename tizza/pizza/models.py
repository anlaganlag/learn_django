from django.db import models
from django.contrib.auth.models import User 

class Pizzeria(models.Model):
    owner = models.ForeignKey(User, on_delete=models. CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)
    def __str__(self):
        return self.address

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models. CASCADE)
    def __str__(self):
        return self.title

class Likes(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models. CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
