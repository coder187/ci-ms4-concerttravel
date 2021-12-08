from events.models import EventList, PickLoc
from django.shortcuts import get_object_or_404

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

    
    grand_total = total # for header total
    # print(total)
    # print(product_count)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total
    }

    return context
