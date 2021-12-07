from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings


from .forms import OrderForm

from bag.context import bag_contents

from events.models import PickLoc, EventList
from .models import Order, OrderLineItem

import datetime

import stripe 

def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    #print('keys:') 
    #print(stripe_public_key)
    #print(stripe_secret_key)
    bag = request.session.get('bag', {})

    if request.method == 'POST':
        print('POST VALIDATNG FORM')
        print(datetime.datetime.now())
   
        # capture order header from the form
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()

            # iterate over the bag items and add to db
            # item_id = event_id:pickloc_id, item_data = qty
            for item_id, item_data in bag.items():
                event_id = item_id.split(':')[0]
                pickloc_id = item_id.split(':')[1]
                pickloc_model = PickLoc.objects.get(id=pickloc_id) 
                fare = pickloc_model.fare
                eventlist_model = EventList.objects.get(id=event_id)
                qty = int(item_data)
                
                i=0
                for i in range(qty):
                    order_line_item = OrderLineItem(
                        order=order,
                        event=eventlist_model,
                        pickloc=pickloc_model,
                        price=fare
                        )
                    order_line_item.save()
                    
                    # print(f"event id:{event_id} pickloc_id:{pickloc_id}")
                    # print(f"ticket no: {item_data}")
                    # print(f"fare: {fare}")

                    i +=1

    if not bag:
        # messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('events'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            )
    print(intent)



    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)