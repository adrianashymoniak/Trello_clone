from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

from api.views.column_view import ColumnsListView, ColumnDetailView
from api.views.project_view import ProjectsListView, ProjectDetailView
from api.views.task_view import TaskListView, TaskDetailView

API_TITLE = 'Trello clone api'

docs = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view = include_docs_urls(title=API_TITLE)

urlpatterns = [
    path('projects', ProjectsListView.as_view()),
    path('projects/<int:projects_id>/', ProjectDetailView.as_view()),
    path('projects/<int:project_id>/columns/', ColumnsListView.as_view()),
    path('projects/<int:project_id>/columns/<int:pk>/',
         ColumnDetailView.as_view()),
    path('projects/<int:project_id>/tasks/', TaskListView.as_view()),
    path('projects/<int:project_id>/tasks/<int:pk>/',
         TaskDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('schema/', schema_view),
    path('docs/', docs.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

]
