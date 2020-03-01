from rest_framework import serializers

from api.models.column import Column


class ColumnSerializer(serializers.ModelSerializer):
    column_id = serializers.IntegerField(source='id', read_only=True)
    order = serializers.IntegerField()

    class Meta:
        model = Column
        fields = ['column_id', 'title', 'project', 'order']
