from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(render,'home/home.html', {})




#def index(request):
#    return HttpResponse("It is working!")
