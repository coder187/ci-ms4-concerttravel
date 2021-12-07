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


@register.simple_tag(name='multiple_args_tag')
def multiple_args_tag(a, b, c, d):
   print (a)
   print (b)
   print (c)
   return

@register.simple_tag(name='get_ticket_qty')
def get_ticket_qty(order_number,event,pickloc):
    order = get_object_or_404(Order, order_number=order_number)
    #for item in order.lineitems.all():
    #    print (item.event.name)
    #arg_list = [arg.strip() for arg in args.split(',')]
    #event = arg_list[1]
    #pickloc = arg_list[2]
    #print (args)
    
    #event = args.split(':')[0]
    #pickloc = args.split(':')[1]
    ticket_count= order.lineitems.filter(event=event,pickloc=pickloc).count()
    # {% get_ticket_qty order.order_number item.event.id item.pickloc.id  %}
    return ticket_count

