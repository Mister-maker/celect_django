from django.shortcuts import get_object_or_404, render

from .models import Project

# Create your views here.
def projects_view(request, *args, **kwargs):
    projects = Project.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'projects': projects
    }
    return render(request, "projects.html", context)


def project(request, project_id, *args, **kwargs):
    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project
    }
    return render(request, "single_project.html", context)