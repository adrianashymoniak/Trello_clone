from rest_framework import serializers

from api.models.column import Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('title', 'project')
