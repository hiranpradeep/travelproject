from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['Username']
        password = request.POST['Password1']
        user= auth.authenticate(username=username,password=password)
        if user is not None :
           auth.login(request,user)
           return redirect('/')
        else:
            messages.info(request,"Invalid credential")
            return redirect('login')
    return render (request,'login.html')
def register(request):
    if request.method== 'POST':
        username=request.POST['Username']
        firstname=request.POST['Firstname']
        lastname=request.POST['Lastname']
        email=request.POST['Email_id']
        password=request.POST['Password1']
        cpassword=request.POST['Password2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,'email id already exist')
                return redirect('register')
            user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
            user.save();
            return redirect('login')
            print("User Created")
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout (request)
    return redirect ('/')