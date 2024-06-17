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
    path('', views.index, name='index'),  # 메인 페이지
    path('new_game/', views.new_game, name='new_game'),  # 새로운 게임 선택
    
    path('snake-game/', views.snake_game_view, name='snake_game_view'),
    path('tictactoe-game/', views.tictactoe_game_view, name='tictactoe_game_view'),
    path('typing-game/', views.typing_game_view, name='typing_game_view'),
    path('flappy-game/', views.flappy_game_view, name='flappy_game_view'),
    
    path('login/', views.login_view, name='login'),  # 로그인 페이지 렌더링
    path('login/submit/', views.user_login, name='user_login'),  # 로그인 처리
    path('join/', views.create_user, name='join'),  # 회원가입 처리
    path('create/', views.create_user, name='create_user'),

    path('app/', include('MSGapp.urls')),  # 'admin URL. 유저 확인하게 만듦. 

]
