from rest_framework import generics, permissions

from api.models.column import Column
from api.serializers.column_serializers import ColumnSerializer


class ColumnsListView(generics.ListCreateAPIView):
    serializer_class = ColumnSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        queryset = Column.objects.filter(project_id=project_id)
        return queryset

    def perform_create(self, serializer):
        project_id = self.kwargs["project_id"]
        serializer.save(project_id=project_id)


class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = (permissions.IsAuthenticated,)
