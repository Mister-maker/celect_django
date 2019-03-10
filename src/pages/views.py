from django.shortcuts import render

from projects.models import Project
from team.models import Team
from achievement.models import Achievement
from event_listing.models import Event

def home_view(request, *args, **kwargs):
    projects = Project.objects.order_by('-list_date').filter(is_published=True)[:6]
    team_members = Team.objects.all().filter(is_published=True)[:6]
    achievements = Achievement.objects.order_by('-list_date').filter(is_published=True)[:1]
    events = Event.objects.order_by('-list_date').filter(is_published=True)[:1]

    context = {
        'projects': projects,
        'team_members': team_members,
        'achievements': achievements,
        'events': events
    }
    return render(request, "home.html", context)


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def curriculum_view(request, *args, **kwargs):
    return render(request, "curriculum.html", {})

