import uuid

from django.db import models
from django.db.models import Sum

from events.models import EventList, PickLoc
# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self): # use of _ indictes private method only to be used inside this class.
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()  # random unique 32 chars

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('price'))['price__sum']
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.PROTECT, related_name='lineitems')
    event = models.ForeignKey(EventList, null=False, blank=False, on_delete=models.PROTECT)
    pickloc = models.ForeignKey(PickLoc, null=False, blank=False, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    pax_fullname = models.CharField(max_length=50, null=True, blank=True)
    pax_email = models.CharField(max_length=50, null=True, blank=True)
    pax_tel = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return f'Event_ID: {self.event.id} on order {self.order.order_number}'
