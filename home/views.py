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
            body = cd.get('message')
            cust_email = cd.get('from_email')
            print('start email')
            try:
                send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
                )
                print('email semt')
            except Exception as e:
                print('error')   
                print(e)
    
    template = 'home/index.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
        
