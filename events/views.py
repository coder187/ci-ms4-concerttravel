from django.shortcuts import render, get_object_or_404
from .models import EventList, PickLoc
# Create your views here.

# Create your views here.
def all_events(request):
    ''' a view to show all events, inc sorting and search query'''

    events = EventList.objects.all()  # get all events
  

    context = {
        'events':events,
    }

    return render(request, 'events/events.html', context)
    

def event_detail(request, event_id):
    ''' a view to show individual event'''

    event = get_object_or_404(EventList, pk=event_id)
    picklocs = PickLoc.objects.all()
    context = {
            'event': event,
            'picklocs':picklocs
        }

    return render(request, 'events/event_detail.html', context)
    
