from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    form = LoginForm(request.POST)
    if request.method == "POST":
        if user is not None:
            login(request, user)
        #render(request, 'accounts/login.html', {'messages': messages}, {'form': form})
            return HttpResponseRedirect(reverse('index:index'))

        else:
            return render(request, 'accounts/login.html', {'messages': messages}, {'form': form})
    else:
        return render(request, 'accounts/login.html', {'messages': messages}, {'form': form})