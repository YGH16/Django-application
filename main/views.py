from django import http
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Models to use
from .models import Report, User, serviceUpdate, Profile, QuarterlyReport, SupportTicket, ClientAgreement

appname = 'Blackwell Investor Portal AIF '

# Login View
def loginUser(request):

    # Check for POST Request
    if 'Username' in request.POST and 'Password' in request.POST:
        username= request.POST['Username']
        password = request.POST['Password']

        user = authenticate(username=username, password=password)
        # Check user exists
        if user is None:
            # if user doesn't exist redirect user back to login and display message
            messages.error(request, 'Incorrect Login Details, Please Try Again')
            return redirect('/')
        else:
            # if user exists then redirect user to home page
            login(request, user)
            return redirect('/home')
            
    # On GET Request return the login page
    context = {'appname': appname}
    return render(request, 'main/login.html', context)


# Home View
@login_required(login_url='/')
def home(request):
    if request.user.is_authenticated:
        # Get all service Messages
        serviceMessages= serviceUpdate.objects.all()
        context = {'user': request.user, 'serviceMessages': serviceMessages, 'appname': appname}
        return render(request, 'main/home.html', context)
    else:
        messages.error(request, 'Something Went Wrong, Please Try Login Again')
        return redirect('/')


# Profile View
@login_required(login_url='/')
def ProfilePage(request):
    if request.user.is_authenticated:
        # Access Users Profile
        userProfile = Profile.objects.filter(user=request.user)
        print(userProfile)
        context = {'user': request.user, 'profile': userProfile, 'appname': appname}
        return render(request, 'main/profile.html', context)
    else:
        messages.error(request, 'Something Went Wrong, Please Try Logging In Again')
        return redirect('/')

# Agreements View
@login_required(login_url='/')
def agreements(request):
    if request.user.is_authenticated:
        agreements = ClientAgreement.objects.filter(user=request.user)
        context = {'appname': appname, 'user': request.user, 'agreements': agreements}
        return render(request, 'main/agreements.html', context)
    else:
        messages.error(request, 'Something Went Wrong, Please Try Logging In Again')
        return redirect('/')

# Reports View
@login_required(login_url='/')
def reports(request):
    if request.user.is_authenticated:
        report = Report.objects.filter(user=request.user)
        qreport = QuarterlyReport.objects.filter(user=request.user)
        context = {'user': request.user, 'reports':report, 'quarterlyreports':qreport ,'appname': appname}
        return render(request, 'main/reports.html', context)
    else:
        messages.error(request, 'Something Went Wrong, Please Try Login Again')
        return redirect('/')

# Support View
@login_required(login_url='/')
def support(request):
    if request.user.is_authenticated:
        # check support-subject and support-details exist in the POST request
        if 'Support-Subject' in request.POST and 'Support-Details' in request.POST:
            supportSubject = request.POST['Support-Subject']
            supportDetails= request.POST['Support-Details']
            
            try:
                SupportTicket.objects.create(email=request.user.email, subject=supportSubject, detail=supportDetails)
                messages.success(request, 'Support Ticket Was Successfully Filed')
                return redirect('/support')
            except Exception as e:
                messages.error(request, 'Something Went Wrong Support Was Not Filed')
                return redirect('/support')
        else:
            context = {'appname':appname, 'user': request.user}
            return render(request, 'main/support.html', context)
    else:
        messages.error(request, 'Something Went Wrong, Please Try Login Again')
        return redirect('/')



@login_required(login_url='/')
def logoutUser(request):
    logout(request)
    # successfully logged out message
    messages.success(request,'Successfully Logged Out')
    return redirect('/')


