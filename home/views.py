from django.shortcuts import render

# Create your views here.
def index(request):
    #images = ["image1", 'image2', 'image3']
    
    #return render(request, 'home/index.html', {'images': images})
    return render(request, 'home/index.html')

