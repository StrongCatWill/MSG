from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/submit/', views.user_login, name='user_login'),
    path('join/', views.create_user, name='join'),
    path('create/', views.create_user, name='create_user'),
    path('new_game/', views.new_game, name='new_game'),  # new_game URL 패턴 추가
    path('continue/', views.continue_game, name='continue_game'),  # continue_game URL 패턴 추가
]