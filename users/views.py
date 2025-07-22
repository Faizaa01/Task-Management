from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import CustomRegistrationForm, RegisterForm
from django.contrib.auth import login, authenticate, logout



def sign_up(request):
    form = CustomRegistrationForm()
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is not valid")
    return render(request, 'Registration/register.html', {"form": form})


def sign_in(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'Registration/login.html')




def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign_in')
    

    