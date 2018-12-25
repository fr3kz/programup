from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.models import User
#own apps
from .models import Profile
from .forms import LoginForm



#function to authenticate users by username
def login(request):
    if request.method == 'POST': 
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.info(request,'Pomyslne logowanie')
                return redirect('register')
            else:
                messages.error(request,'Niepoprawne dane')
                return redirect('login')    
    return render(request,'accounts/login.html')        

#function to reigtser new users
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        github = request.POST['github']
        profile_image = request.POST['image']

        if User.objects.filter(username=username).exists():
            messages.error(request,'Ten nick jest zajęty')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            profile = Profile(user=user,profile_image=profile_image,name=name,github=github)
            profile.save()
            auth.login(request,user)
            messages.success(request,'Zarejestrowano')
            return redirect('')
    return render(request,'accounts/register.html')

#function to change user or profile attributes
def edit(request,user_id):
    if request.method == 'POST':
        user = User.objects.get(user_id=user_id)
        github = request.POST['github']
        #profile_image = image
        user.profile.github = github
        user.profile.save()
        return redirect('')
    return 