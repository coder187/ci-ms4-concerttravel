from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.db.models.functions import Lower
from django.db.models import Count


from .models import EventList, PickLoc, Destination, EventType
from checkout.models import Order, OrderLineItem 
from datetime import datetime, timedelta

from .forms import EventListForm, PickLocsForm

# Create your views here.
def all_events(request):
    ''' a view to show all events, inc sorting and search query'''


    # build a list of total tickes sold per event

    # get all events with an event date bewtween today and today+days_to_show
    # and where publish = true

    
    if hasattr(settings, 'DAYS_TO_SHOW'):
        days_to_show = int(settings.DAYS_TO_SHOW)
    else:
        days_to_show = 365
    
    from_date = datetime.today().date()
    to_date = from_date + timedelta(days=days_to_show)
    
    if request.user.is_superuser:
         events = EventList.objects.filter(
            event_date__range=[from_date, to_date]).order_by(
                'event_date')
    else:   
        events = EventList.objects.filter(
            event_date__range=[from_date, to_date],
                publish = True).order_by(
                'event_date')

    
    # query for total tickets per event
    ticket_totals_per_event = EventList.objects.filter(publish=True).annotate(number_of_tickets=Count('eventrecord'))

    t_sum = 0
    t_count = 0
    average_tickets = 0
    if ticket_totals_per_event.count() > 0:
        for t in ticket_totals_per_event:
            t_sum = t_sum + t.number_of_tickets
            t_count +=1
    
    average_tickets = t_sum/t_count
        
    query = None
    locations = None
    types = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            events = events.order_by(sortkey)


        
        if 'location' in request.GET:
            locations = request.GET['location'].split(',')
            if request.user.is_superuser:
                events = EventList.objects.filter(event_dest__destination__in=locations, \
                    event_date__range=[from_date, to_date]).order_by('event_date')
            else:
                events = EventList.objects.filter(event_dest__destination__in=locations, \
                    event_date__range=[from_date, to_date], \
                    publish=True).order_by('event_date')
                
            locations = Destination.objects.filter(destination__in=locations)

        if 'event_type' in request.GET:
            types = request.GET['event_type'].split(',')
            if request.user.is_superuser:
                events = EventList.objects.filter(event_type__event_type__in=types, \
                    event_date__range=[from_date, to_date]).order_by('event_date')
            else:
                events = EventList.objects.filter(event_type__event_type__in=types, \
                    event_date__range=[from_date, to_date], \
                    publish=True).order_by('event_date')
                
            types = EventType.objects.filter(event_type__in=types)
        

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('events'))
            
            queries = Q(name__icontains=query) \
                    | Q(description__icontains=query) \
                    | Q(event_dest__friendly_name__icontains=query) \
                    | Q(event_type__friendly_name__icontains=query)

            events = EventList.objects.filter(queries, \
                event_date__range=[from_date, to_date], \
                    publish=True).order_by('event_date')

    context = {
        'events':events,
        'search_term': query,
        'current_locations': locations,
        'current_types':types,
        'ticket_totals_per_event':ticket_totals_per_event,
        'average_tickets':average_tickets

    }

    return render(request, 'events/events.html', context)
    

def event_detail(request, event_id):
    ''' a view to show individual event'''

    event = get_object_or_404(EventList, pk=event_id)
    picklocs = PickLoc.objects.all().order_by('sort')
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

@login_required
def add_pick(request):
    """ Add a pick up loaction """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PickLocsForm(request.POST)
        if form.is_valid():
            pick = form.save()
            messages.success(request, 'Successfully added pick location!')
            return redirect(reverse('events'))
        else:
            messages.error(request, 'Failed to add pick location. Please ensure the form is valid.')
    else:
        form = PickLocsForm()
        picklocs = PickLoc.objects.all()

    template = 'events/add_pick.html'
    context = {
        'form': form,
        'picklocs':picklocs,
    }

    return render(request, template, context)

@login_required
def edit_pick(request,pick_id):
    """ Edit a pick up location in the store """
    # print ('edit pick started')

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))


    pickloc = get_object_or_404(PickLoc,pk=pick_id)

    if request.method == 'POST':
        form = PickLocsForm(request.POST, instance=pickloc)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated pick location!')
            return redirect(reverse('events'))
        else:
            messages.error(request, 'Failed to update pick location. Please ensure the form is valid.')
    else:
        form = PickLocsForm(instance=pickloc)
        messages.info(request, f'You are editing {pickloc.location}')
    
    template = 'events/edit_pick.html'
    context = {
            'form': form,
            'pickloc': pickloc,
        }
    return render(request, template, context )

@login_required
def delete_pick(request, pick_id):
    """ Delete an pick location from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    pickloc = get_object_or_404(PickLoc,pk=pick_id)
    try:
        pickloc.delete()
        messages.success(request, 'Pick Location deleted!')
    except Exception as e:
        messages.error(request, 'Failed to delete Event!')
    
    
    return redirect(reverse('events'))