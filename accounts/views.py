from django.shortcuts import render,redirect
# optional  from django.contrib.auth import authenticate,login
from django.contrib import auth

#function to authenticate users by username
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username,password=password)

        if user is not None:
            auth.login(request,user)
            redirect('')
        else:
            # TODO: user wrong data
            return    
    return render(request,'accounts/login.html')

#function to reigtser new users
def register(request):
    if request.method == 'POST':
        #TODO: handle register form
        return
    return    