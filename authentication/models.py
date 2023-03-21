# models.py
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    youtube_link = models.URLField(max_length=255)
