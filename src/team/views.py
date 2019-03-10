from django.shortcuts import render

from .models import Team

# Create your views here.
def team_view(request, *args, **kwargs):
    team_members = Team.objects.all().filter(is_published=True)
    context = {
        'team_members': team_members
    }
    return render(request, "team.html", context)