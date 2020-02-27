from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
