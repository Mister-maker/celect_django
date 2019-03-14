from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_view, name="projects"),
    path('<int:project_id>', views.project, name="project"),
]