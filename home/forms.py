from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(required=True)
    

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'from_email': 'Email',
            'message': 'Your Message',
        }

        for field in self.fields:
            placeholder = f'{placeholders[field]} *'            
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-sm'
            self.fields[field].label = False
        