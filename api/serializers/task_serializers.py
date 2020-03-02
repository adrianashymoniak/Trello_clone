from django.contrib.auth.models import User
from rest_framework import serializers

from api.models.task import Task
from api.serializers.user_serializer import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    assigned = serializers.SlugRelatedField(many=True, slug_field='username',
                                            queryset=User.objects.all())

    class Meta:
        model = Task
        fields = [
            'project', 'title', 'description', 'column', 'author', 'assigned']
