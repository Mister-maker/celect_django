from django.shortcuts import get_object_or_404, render
from .models import Event

def event_view_index(request, *args, **kwargs):
    events = Event.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'events': events
    }
    return render(request, 'events/events.html', context)

def event(request, event_id, *args, **kwargs):
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event
    }
    return render(request, 'events/event.html', context)


