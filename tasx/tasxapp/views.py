from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
# Create your views here.

def index(request):
    return render(request,'home/home.html', {})




#def index(request):
#    return HttpResponse("It is working!")
