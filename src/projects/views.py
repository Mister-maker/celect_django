from django.shortcuts import render

from .models import Project

# Create your views here.
def projects_view(request, *args, **kwargs):
    projects = Project.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'projects': projects
    }
    return render(request, "projects.html", context)