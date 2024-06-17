from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.contrib import messages
import subprocess
import os


def index(request):
    return render(request, 'index.html')

def new_game(request):
    return render(request, 'new_game.html')

def snake_game_view(request):
    return render(request, 'snake_game.html')

def tictactoe_game_view(request):
    return render(request, 'tictactoe_game.html')

def typing_game_view(request):
    return render(request, 'typing_game.html')

def flappy_game_view(request):
    return render(request, 'flappy_game.html')

def login_view(request):
    return render(request, 'login.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)  # commit=True로 변경
            return redirect('index')  # 회원가입 후 리다이렉트할 URL
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def join(request):
    return render(request, 'user_form.html')

def user_login(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 로그인 후 리다이렉트할 URL
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')