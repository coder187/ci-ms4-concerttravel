from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    '''A view that renders the bags contents '''
    return render(request, 'bag/bag.html')

def add_to_bag(request, event_id):
    '''Add a ticket for the given event to the bag '''

    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # get the session bag or create one if 
    # does not exist and initialise it to an empty dict
    bag = request.session.get('bag', {})
    
    if event_id in list(bag.keys()):
        bag[event_id] += qty
    else:
        bag[event_id] = qty  # event_id:qty

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


