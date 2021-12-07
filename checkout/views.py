from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from events.models import EventList
# from profiles.models import UserProfile
# from profiles.forms import UserProfileForm
from bag.context import bag_contents

import stripe
import json
import datetime

@require_POST
def cache_checkout_data(request):
    try:
        print('cache checkout started')
        # get the payment intent identifier for the intent in this request
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # modify payment intent - adding meta data (user, save(true/false), shopping bag)
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        # intent modified so rtn 200 ok
        print('cache checkout completed')
        return HttpResponse(status=200)
    except Exception as e:
        print('cache checkout error')
        print(e.message)
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)

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
                try:

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
                except EventList.DoesNotExist:
                    messages.error(request, (
                        "One of the events in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        print('START STRIPE INTENT')
        print(datetime.datetime.now())
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

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)