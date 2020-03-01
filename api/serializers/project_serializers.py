from rest_framework import serializers

from api.models.column import Column
from api.models.project import Project
from api.serializers.column_serializers import ColumnSerializer
from api.serializers.user_serializer import UserSerializer


class ProjectsListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    project_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Project
        fields = ['project_id', 'title', 'author']


class ProjectDetailSerializer(ProjectsListSerializer):
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Project
        fields = ['project_id', 'title', 'author', 'columns']

    def create(self, validated_data):
        columns_data = validated_data.pop('columns')
        project = Project.objects.create(**validated_data)
        for column_data in columns_data:
            Column.objects.create(project=project, **column_data)
        return project

    def update(self, instance, validated_data):
        columns_data = validated_data.pop('columns')
        columns = instance.columns.all()
        columns = list(columns)
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        for column_data in columns_data:
            column = columns.pop(0)
            column.title = column_data.get('title', column.title)
            column.save()
        return instance
