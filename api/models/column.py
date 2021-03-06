from django.db import models
from ordered_model.models import OrderedModel

from api.models.project import Project


class Column(OrderedModel):
    title = models.CharField(max_length=255, blank=True)
    project = models.ForeignKey(Project, related_name='columns',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.title
