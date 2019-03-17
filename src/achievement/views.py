from django.shortcuts import get_object_or_404, render

from .models import Achievement

def achievement_view(request, *args, **kwargs):
    achievements = Achievement.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'achievements': achievements
    }
    return render(request, "achievement.html", context)


def achievement(request, achievement_id, *args, **kwargs):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    context = {
        'achievement': achievement
    }
    return render(request, "single_achievement.html", context)