from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineitemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('ticket_no',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineitemAdminInLine,)

    readonly_fields = ('order_number', 'date', 'order_total')
    
    # will allow us to specify the order of the fields in the admin interface
    fields = ('order_number', 'user_profile', 'date', 'full_name','email',
                'phone_number', 'country', 'postcode', 'town_or_city',
                'street_address1','street_address2',
                'county','order_total',
                'original_bag','stripe_pid')# To restrict the columns that show up in the order list to only a few key items.
    list_display = ('id','order_number', 'date', 'full_name','order_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
