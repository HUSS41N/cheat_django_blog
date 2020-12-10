from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                #message pop up
                return redirect('singup')
            else:
                if User.objects.filter(email=email).exists():
                    #message pop up
                    return redirect('signup')
                else:
                    user = User(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
                    user.set_password(password)
                    user.save()
                    return redirect('signin')
        else:
            #message pop up passwords must match 
            return redirect('signup')
    else:
        return render(request,'User/sign-up.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            #pop up login success
            print('LOGGIN')
            return redirect('index')
        else:
            #pop up invalid credintials
            print('Failed')
    else:
        return render(request,'User/login.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('Loggedout')
        return redirect('index')