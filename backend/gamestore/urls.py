from django.urls import path

from . import views

urlpatterns = [
    path('', views.gamestore, name = 'index'),
    path('games/', views.games, name = 'games'),
    path('games/<int:game_id>/', views.game, name = 'game'),
    path('genres/', views.genres, name = 'genres'),
    path('genres/<int:genre_id>/', views.genre, name='genre'),
]
