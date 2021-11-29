from django.contrib import admin

from .models import EventList, EventType, PickLoc, Destination

# Register your models here.
admin.site.register(EventList)
admin.site.register(EventType)
admin.site.register(PickLoc)
admin.site.register(Destination)
