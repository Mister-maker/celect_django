from django.shortcuts import render

from .models import Achievement

def achievement_view(request, *args, **kwargs):
    achievements = Achievement.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'achievements': achievements
    }
    return render(request, "achievement.html", context)

