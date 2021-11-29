from django.db import models

class PickLoc(models.Model):
    ''' list of pick up locations or bus stops '''
    location = models.CharField(max_length=254)
    pick_time = models.CharField(max_length=20, default='14:00')
    sort = models.IntegerField(default=0)
    fare = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_upper_name(self):
        return self.friendly_name.upper

class EventType(models.Model):
    ''' concert/festival/sporting etc.. '''
    event_type = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_upper_name(self):
        return self.friendly_name.upper


class Destination(models.Model):
    ''' list of venues '''
    destination = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_upper_name(self):
        return self.friendly_name.upper

class EventList(models.Model):
    event_type = models.ForeignKey('EventType', on_delete=models.PROTECT)
    event_dest = models.ForeignKey('Destination', on_delete=models.PROTECT)
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    event_date = models.DateField()
    publish = models.BooleanField(default=True)
    long_desc = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
