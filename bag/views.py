from django.shortcuts import render, redirect, reverse, HttpResponse,get_object_or_404
from django.contrib import messages
from events.models import EventList, PickLoc

from datetime import datetime


# Create your views here.
def view_bag(request):
    '''A view that renders the bags contents '''
    return render(request, 'bag/bag.html')

def add_to_bag(request, event_id):
    '''Add a ticket for the given event to the bag '''

    event = get_object_or_404(EventList, pk=event_id)
    pickloc = request.POST.get('pick-loc')
    pick_loc_desc = get_object_or_404(PickLoc, pk=pickloc)

    formatted_eventdate = event.event_date.strftime("%b/%d")

    qty = int(request.POST.get('quantity'))
    
    event_pickloc = event_id + ':' + pickloc
    redirect_url = request.POST.get('redirect_url')

    # get the session bag or create one if
    # does not exist and initialise it to an empty dict
    bag = request.session.get('bag', {})
    
    if event_pickloc in list(bag.keys()):
        bag[event_pickloc] += qty
        messages.success(request, f'Updated {event.name} {formatted_eventdate} [{pick_loc_desc}]')
    else:
        messages.success(request, f'Added {event.name} {formatted_eventdate} [{pick_loc_desc}] to your bag')
        bag[event_pickloc] = qty  # 'event_id:pickloc':qty

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)

def adjust_bag(request, combination_key):
    '''Adjust the ticket qty for the given event to the specified quantity '''

    qty = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if qty > 0:
        bag[combination_key] = qty
        messages.success(request, f'Updated {event.name} {formatted_eventdate} [{pick_loc_desc}]')
    else:
        bag.pop(combination_key)
        messages.success(request, f'Removed {event.name} {formatted_eventdate} from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
            

def remove_from_bag(request, combination_key):
    '''Remove the ticket from the shopping bag '''

    try:

        bag = request.session.get('bag', {})

        bag.pop(combination_key)
        messages.success(request, f'Removed {event.name} {formatted_eventdate} from your bag.')
        
        request.session['bag'] = bag

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
