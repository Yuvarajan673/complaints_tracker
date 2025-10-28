import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.
def home(request):
    recentcomplaints=Complaint.objects.all().order_by('-creation_date')
    return render(request,"home.html",{'recentcomplaints':recentcomplaints})

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
        else:
            return HttpResponse('Inavlid User')
    return redirect('/') 

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if username and email and password1 and password2:
            if password1 == password2:
                if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists() :
                    user=User.objects.create_user(username=username,email=email,password=password1)
                    user.save()
                else:
                    return HttpResponse("Username or Email are already taken")
            else:
                return HttpResponse("Passwords are not match")
        else:
            return HttpResponse("The fields are not to be null")
    return redirect('/') 


def submit_complaint(request):
    if request.method=='POST':
        title=request.POST.get('complaint-title')
        category=request.POST.get('category')
        description=request.POST.get('complaint-description')
        location=request.POST.get('address')
        image=request.FILES.get('complaint-image')
        complaint=Complaint.objects.create(
            user=request.user,
            title=title,
            category=category, 
            description=description,
            location=location,
            image=image
        )

    return HttpResponse("Complaint Submitted")



def delete(request,id):
    complaint=Complaint.objects.get(id=id)
    complaint.delete()
    return redirect('mycomplaints')



def allcomplaints(request):
    complaints=Complaint.objects.all().order_by('-creation_date')
    return render(request,'allcomplaints.html',{'complaints':complaints})


def filtercity(request):
    city = request.GET.get('city')
    if city:
        pass
    return redirect('allcomplaints')


def mycomplaints(request):
    mycomplaint=Complaint.objects.filter(user=request.user)
    return render(request,'mycomplaints.html',{'mycomplaint':mycomplaint})



def complaintdetails(request,id):
    complaintdetail=Complaint.objects.get(id=id)
    return render(request,'complaintdetails.html',{'complaintdetail':complaintdetail})