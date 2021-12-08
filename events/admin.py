from django.contrib import admin

from .models import EventList, EventType, PickLoc, Destination




class EventListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'event_date',
        'description',
        'event_dest',
    )

    ordering = ('event_date', 'name')

# Register your models here.
admin.site.register(EventList, EventListAdmin)
admin.site.register(EventType)
admin.site.register(PickLoc)
admin.site.register(Destination)
