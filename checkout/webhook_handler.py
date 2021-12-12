from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from events.models import EventList, PickLoc
from profiles.models import UserProfile


import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        # print ('send email started')
        # print (order.order_number)

        ol = OrderLineItem.objects.filter(order_id=order.id).order_by('-ticket_no')
          
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL,'ol':ol})
        
        print ('send mail')
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        
        print ('send mail COMPLETED')


    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # print('handle_payment_intent_succeeded started')
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                # ieact exact match case insensitive
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid, 
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            # print ('call send mail')
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                    user_profile=profile

                )
                for item_id, item_data in json.loads(bag).items():
                    event_id = item_id.split(':')[0]
                    pickloc_id = item_id.split(':')[1]
                    pickloc_model = PickLoc.objects.get(id=pickloc_id) 
                    fare = pickloc_model.fare
                    eventlist_model = EventList.objects.get(id=event_id)
                    qty = int(item_data)
                    #print (event_id)
                    #print (pickloc_id)
                    i=0
                    for i in range(qty):
                        order_line_item = OrderLineItem(
                        order=order,
                        event=eventlist_model,
                        pickloc=pickloc_model,
                        price=fare
                        )
                    order_line_item.save()
                    i +=1
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # print ('send maik -oder not in db')
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)