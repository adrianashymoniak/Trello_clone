from rest_framework import generics, permissions

from api.models.task import Task
from api.serializers.task_serializers import TaskSerializer


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        queryset = Task.objects.filter(project_id=project_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
