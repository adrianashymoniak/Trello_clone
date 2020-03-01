from rest_framework import generics, permissions

from api.models.project import Project
from api.serializers.project_serializers import ProjectsListSerializer, \
    ProjectDetailSerializer


class ProjectsListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
