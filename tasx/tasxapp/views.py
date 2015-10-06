from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Report

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from .models import User
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login , logout, authenticate


@login_required(login_url='/tasxapp/login/')
def index(request):
    reports = Report.objects.order_by('-date').all()
    return render(request,'home/home.html', {'reports' : reports})

@login_required(login_url='/tasxapp/login/')
def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request,'home/post_detail.html', {'report' : report})



#Authenticated
def login_v(request): #Log in View
    msg=''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/tasxapp')
    else:
        if request.method=="POST":
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                auth_user=authenticate(username=username,password=password)
                if auth_user is not None and auth_user.is_active:
                    login(request,auth_user)
                    return redirect('/tasxapp')
                else:
                    msg='Wrong Email and password combination.'
        form=LoginForm()
        ctx={'form':form,'mensaje':msg}
        return render(request,'home/login.html', ctx)


#Registration
def sign_up(request):
    msg=''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/tasxapp')
    else:
        if request.method=="POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                name=form.cleaned_data['name']
                lastname=form.cleaned_data['lastname']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                new_u=User.objects.create_user(username= email, email= email, password=password)
                new_u.first_name=name
                new_u.last_name=lastname
                new_u.save()
                new_user = authenticate(email=email,password=password)
                if new_user is not None :
                    login(request,new_user)
                    new_p=UserProfile.objects.create(user=new_u,carrera=carrera)
                    new_p.save()
                    return redirect('/tasxapp/')
                else:
                    msg='Wrong'

        ctx={'form':RegistrationForm,'msg':msg}
        return render(request,'home/singup.html', ctx)


@login_required(login_url='/tasxapp/login/')
def logout_v(request):
    logout(request)
    return redirect('/tasxapp')
