from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Report
# Create your views here.

def index(request):
    try:
        reports = Report.objects.all()
        ##reports = Report.objects.filter(date=timezone.now()).order_by('date')
    except Report.DoesNotExist:
        raise Http404("Theres no reports.")
    return render(request,'home/home.html', {'reports' : reports})


#def index(request):
#    return HttpResponse("It is working!")
