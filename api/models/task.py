from django.contrib.auth.models import User
from django.db import models

from api.models.column import Column
from api.models.project import Project


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    project = models.ForeignKey(Project, related_name='project_tasks',
                                on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned = models.ManyToManyField(User, related_name='assigned_users')
    column = models.ForeignKey(Column, related_name='tasks',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title
