"""
URL configuration for MSGdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  
from MSGapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),    # 메인 
    path('new_game/', views.new_game, name='new_game'), # 새로운 게임 선택
    path('snake-game/', views.snake_game_view, name='snake_game_view'),
    path('tictactoe-game/', views.tictactoe_game_view, name='tictactoe_game_view'),
    path('typing-game/', views.typing_game_view, name='typing_game_view'),
    path('memory-game/', views.memory_game_view, name='memory_game_view'),
    path('run-snake/', views.run_snake_script, name='run_snake_script'), # snake 게임 시작
]
