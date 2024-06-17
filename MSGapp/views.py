from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import subprocess
import os

def index(request):
    return render(request, 'index.html')

def new_game(request):
    return render(request, 'new_game.html')

@login_required(login_url='login')  # 로그인되지 않았을 경우 로그인 페이지로 리디렉션
def continue_game(request):
    return redirect('new_game')  # 로그인된 경우 게임 선택 페이지로 리디렉션

def snake_game_view(request):
    return render(request, 'snake_game.html')

def tictactoe_game_view(request):
    return render(request, 'tictactoe_game.html')

def typing_game_view(request):
    return render(request, 'typing_game.html')

def flappy_game_view(request):
    return render(request, 'flappy_game.html')

def connect_game_view(request):
    return render(request, 'connect.html')

def pacman_game_view(request):
    return render(request, 'pacman.html')

def login_view(request):
    return render(request, 'login.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
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
