from events.models import EventList, PickLoc
from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal

def bag_contents(request):

    eventid = 0
    picklocid = 0
    ticket_price = 0
    total = 0
    product_count = 0
    bag_items = [] 
    bag = request.session.get('bag', {})

    for event_id, quantity in bag.items():
        eventid = event_id.split(':')[0]
        picklocid = event_id.split(':')[1]
        pickloc_model = get_object_or_404(PickLoc, pk=picklocid)
        eventlist_model = get_object_or_404(EventList, pk=eventid)
        ticket_price = pickloc_model.fare
        total = total + ticket_price * quantity
        product_count += quantity
        
        bag_items.append({
                'event_id': eventid,
                'pickloc_id': pickloc_model.id,
                'pickloc_name': pickloc_model.location,
                'ticket_quantity': quantity,
                'price_per_ticket': pickloc_model.fare,#
                'price_line': pickloc_model.fare * quantity,
                'eventlist': eventlist_model,
                'combi_key': str(eventid) + ':' + str(pickloc_model.id),

            })
        
    grand_total = total 
    discount = 0
    discount_delta = None
    discount_threshold = None
    discount_percentage = None
    if hasattr(settings, 'DISCOUNT_THRESHOLD') and hasattr(settings, 'STANDARD_DISCOUNT_PERCENTAGE'):
            discount_percentage = settings.STANDARD_DISCOUNT_PERCENTAGE
            discount_threshold = settings.DISCOUNT_THRESHOLD
            if total > discount_threshold:
                discount = total * (Decimal(discount_percentage)/100)
                grand_total = total - discount
            else:
                discount_delta = discount_threshold- total

    else:
            grand_total = total # for header total   

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'discount_threshold': discount_threshold,
        'discount_percentage':discount_percentage,
        'discount_applied':discount,
        'discount_delta':discount_delta,
    }

    return context
