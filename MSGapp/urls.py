from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/submit/', views.user_login, name='user_login'),
    path('join/', views.create_user, name='join'),
    path('create/', views.create_user, name='create_user'),
]