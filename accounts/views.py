from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import get_user_model

User = get_user_model()


def login_view(request):
    form = LoginForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index:index'))

            else:
                return render(request, 'accounts/login.html', {'form': form})
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index:index'))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('index:index'))
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})