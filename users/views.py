from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.
def create_user(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('user')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def user(request):
    return HttpResponse("user page")

def auth_user(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('user')
    else:
        form = AuthenticationForm()
    return render(request,'auth_user.html',{'form':form})

def logout_user(request):
    if request.method=="POST":
        logout(request)
    return redirect("user")
    