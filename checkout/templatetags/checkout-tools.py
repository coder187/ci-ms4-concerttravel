from django import template
from events.models import PickLoc, EventList
from checkout.models import Order, OrderLineItem
from django.shortcuts import get_object_or_404

register = template.Library()

@register.filter(name='hello')
def hello(quantity,price):
    return 'how you doin?'


@register.filter(name='concat_str')
def concat_str(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + ':' + str(arg2)


@register.simple_tag(name='get_ticket_qty')
def get_ticket_qty(order_number,event,pickloc):
    order = get_object_or_404(Order, order_number=order_number)

    ticket_count= order.lineitems.filter(event=event,pickloc=pickloc).count()
    # {% get_ticket_qty order.order_number item.event.id item.pickloc.id  %}
    return ticket_count

