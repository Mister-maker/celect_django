from django.shortcuts import render
from .models import Internship

def internships_view(request, *args, **kwargs):
    internship = Internship.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'internship': internship
    }
    return render(request, "internships.html", context)