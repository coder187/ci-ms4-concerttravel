from django.contrib import admin

from .models import EventList, EventType, PickLoc, Destination


class EventListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'event_date',
        'description',
        'event_dest',
        'image',
        'image_url',
        'publish'
    )

    ordering = ('event_date', 'name')


class PickLocsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'location',
        'pick_time',
        'sort',
        'fare'
    )


#  Register your models here.
admin.site.register(EventList, EventListAdmin)
admin.site.register(EventType)
admin.site.register(PickLoc, PickLocsAdmin)
admin.site.register(Destination)
