from django.contrib import admin

# Register your models here.
from api.models.column import Column
from api.models.project import Project
from api.models.task import Task

models = [Column, Project, Task]

for model in models:
    admin.site.register(model)
