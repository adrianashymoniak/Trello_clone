from rest_framework import serializers

from api.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Project
        fields = ('title', 'author')
