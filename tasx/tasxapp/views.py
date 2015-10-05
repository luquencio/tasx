from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Report
#

def index(request):
    reports = Report.objects.order_by('-date').all()
    return render(request,'home/home.html', {'reports' : reports})

def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request,'home/post_detail.html', {'report' : report})
