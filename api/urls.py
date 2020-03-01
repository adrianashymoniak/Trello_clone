from django.urls import path, include

from api.views.column_view import ColumnsListView, ColumnDetailView
from api.views.project_view import ProjectsListView, ProjectDetailView

urlpatterns = [
    path('projects', ProjectsListView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
    path('projects/<int:project_id>/columns/', ColumnsListView.as_view()),
    path('projects/<int:project_id>/columns/<int:pk>/', ColumnDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),

]
