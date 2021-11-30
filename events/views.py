from django.shortcuts import render
from .models import EventList
# Create your views here.

# Create your views here.
def all_events(request):
    ''' a view to show all events, inc sorting and search query'''

    events = EventList.objects.all()  # get all events

    context = {
        'events':events
    }

    return render(request, 'events/events.html', context)
