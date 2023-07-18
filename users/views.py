from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import Profile


# Create your views here.


def home(request):
    context = {
    }
    return render(request, 'users/home.html', context)


def login_user(request):
    page = 'login'
    context = {
        'page': page
    }

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')

    return render(request, 'users/login_register.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CustomUserCreationForm()
    page = 'register'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Your account was created!')

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occurred during registration!')
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'User logged out!')
    return redirect('login')
