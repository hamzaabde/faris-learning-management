from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)


class Course(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='courses', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = "-created",

    def __str__(self):
        return self.title
