from django.http import JsonResponse
from django.shortcuts import render

def hello_world(request):
    return JsonResponse({'message':'Hello, World!'})

def index(request):
    return render(request, 'index.html')

def new_game(request):
    return render(request, 'new_game.html')