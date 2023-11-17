from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import*
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
import qrcode
# Create your views here.


def register(request):
    if request.method =="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cmpassword=request.POST['cmpassword']
        if password == cmpassword:
            if Login.objects.filter(email=email).exists():
                messages.error(request,"Email is already registered")
                return HttpResponseRedirect("register")
            else:
                hashed_password=make_password(password)
                new_user=Login(firstname=firstname,lastname=lastname,email=email,password=hashed_password)
                new_user.save()
                messages.success(request,"Registration is succesful")
                
                return HttpResponseRedirect('login')
        else:
            messages.error(request,"Password doesn'T MATCH")
            return HttpResponseRedirect("register")
    return render(request,"register.html")



def login(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']

        try:
            user=Login.objects.get(email=email)
        except Login.DoesNotExist:
            messages.error(request,'INvalid email or password')
            return HttpResponseRedirect("login")
        if check_password(password, user.password):
            messages.success(request,"login is suceesfull")
            return HttpResponseRedirect("home")

    return render(request,"login.html")



def home(request):
    return render(request,"home.html")


def generate_qr_code(url):
    qr=qrcode.QRCODE(
        
    )