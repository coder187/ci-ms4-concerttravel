from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            subject = 'message from concert travel.com'
            name = cd.get('from_email')
            from_form_email = cd.get('from_email')
            body = cd.get('message') + '\n' + 'From:' + name + '\n' + 'Email:' + from_form_email 
            cust_email = 'kellyjona@gmail.com'
            form = ContactForm()  #   clear the form
            
            try:
                send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
                )
                
                # copy the sender
                subject = 'Copy of Message from Contact Us Page @ ConcertTravel.com'
                cust_email = from_form_email
                send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
                )
            except Exception as e:
                print(e)
    
    template = 'home/index.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
        
