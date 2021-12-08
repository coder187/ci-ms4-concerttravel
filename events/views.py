from django.shortcuts import render, get_object_or_404
from .models import EventList, PickLoc
from datetime import datetime, timedelta
from django.conf import settings
from .forms import EventListForm

# Create your views here.
def all_events(request):
    ''' a view to show all events, inc sorting and search query'''


    # get all events with an event date bewtween today and today+days_to_show
    # and where publish = true
    if hasattr(settings, 'DAYS_TO_SHOW'):
        days_to_show = int(settings.DAYS_TO_SHOW)
    else:
        days_to_show = 365
    
    from_date = datetime.today().date()
    to_date = from_date + timedelta(days=days_to_show)
    print (from_date)
    print (to_date)
    
    events = EventList.objects.filter(
        event_date__range=[from_date, to_date],
            publish=True).order_by(
            'event_date') 
  
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
    

def add_event(request):
    """ Add a event to the eventList """
    form = EventListForm()
    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
