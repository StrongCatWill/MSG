from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True, null=False)
    password = models.IntegerField(null=False)
    play_score = models.IntegerField(default=0)
    last_play_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=64, null=False)
    description = models.TextField(blank=True)
    required_score = models.IntegerField(null=False)
    last_play_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game_name


class UserGameScore(models.Model):
    user_game_score_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField(null=False)
    play_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.game.game_name} - {self.score}'


class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    session_id = models.CharField(max_length=64, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id
