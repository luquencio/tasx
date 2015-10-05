from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Report
# Create your views here.

def index(request):
    try:
        reports = Report.objects.order_by('-date').all()
    except Report.DoesNotExist:
        raise Http404("Theres no reports.")
    return render(request,'home/home.html', {'reports' : reports})

#def report_detail(request):


#def index(request):
#    return HttpResponse("It is working!")
