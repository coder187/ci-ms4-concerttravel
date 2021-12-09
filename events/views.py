from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError


from .models import EventList, PickLoc
from datetime import datetime, timedelta

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
    

@login_required
def add_event(request):
    """ Add a event to the eventList """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventListForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventListForm()
    
    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit a event in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(EventList, pk=event_id)
    if request.method == 'POST':
        form = EventListForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventListForm(instance=event)
        messages.info(request, f'You are editing {event.name}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """ Delete an event from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    event = get_object_or_404(EventList, pk=event_id)
    try:
        event.delete()
        messages.success(request, 'Event deleted!')
    except Exception as e:
        if ProtectedError:
            messages.error(request, 'Event cannot be deleted as Orders exist!')
        else:
            messages.error(request, 'Failed to delete Event!')
    
    
    return redirect(reverse('events'))
