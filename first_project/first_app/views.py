from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,'first_app/home.html')
def login_redirect(request):
    return render('first_app/home_login.html')
def logout_redirect(request):
    return redirect('first_app/logout.html')
def send_login(request):
    return redirect(request,'first_app/send_login.html')
def hm_login(request):
    return redirect(request,'first_app/hm_login.html')
