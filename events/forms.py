from django import forms
from .models import EventList, PickLoc, EventType, Destination
from .widgets import CustomClearableFileInput

class EventListForm(forms.ModelForm):

    
    class Meta:
        model = EventList
        fields = '__all__'

        image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        picklocs = PickLoc.objects.all()
        eventtypes = EventType.objects.all()
        destinations = Destination.objects.all()
        
        dest_friendly_names = [(d.id, d.get_friendly_name()) for d in destinations]

        self.fields['event_date'].widget=forms.widgets.DateInput(attrs={'type': 'date'})
        self.fields['event_dest'].choices = dest_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            