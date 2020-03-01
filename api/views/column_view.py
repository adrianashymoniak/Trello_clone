from rest_framework import generics

from api.models.column import Column
from api.serializers.column_serializers import ColumnSerializer


class ColumnsListView(generics.ListCreateAPIView):
    serializer_class = ColumnSerializer

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        queryset = Column.objects.filter(project_id=project_id)
        return queryset


class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
