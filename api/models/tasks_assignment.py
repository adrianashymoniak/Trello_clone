from django.contrib.auth.models import User
from django.db import models

from api.models.task import Task


class TasksAssignment(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
