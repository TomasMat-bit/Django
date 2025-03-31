
from django.shortcuts import render, get_object_or_404
from .models import Event

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})
