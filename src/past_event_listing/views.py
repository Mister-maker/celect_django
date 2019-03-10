from django.shortcuts import get_object_or_404, render
from .models import Past_event

def past_event_view_index(request, *args, **kwargs):
    past_events = Past_event.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'past_events': past_events
    }
    return render(request, 'past_events/past_events.html', context)

def past_event(request, past_event_id, *args, **kwargs):
    past_event = get_object_or_404(Past_event, pk=past_event_id)

    context = {
        'past_event': past_event
    }
    return render(request, 'past_events/past_event.html', context)


