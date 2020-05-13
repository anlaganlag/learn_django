from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    User =models.ForeignKey(User,unique=True,on_delete=models.CASCADE)

