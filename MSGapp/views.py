from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
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

def run_snake_script(request):
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'snake_game.py')
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)
        return JsonResponse({'output': result.stdout})
    except Exception as e:
        return JsonResponse({'error': str(e)})