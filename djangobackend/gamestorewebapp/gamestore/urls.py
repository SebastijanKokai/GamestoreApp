from django.urls import path
from . import views

app_name = 'gamestore'


urlpatterns = [
    # Home
    path('', views.index, name = 'index'),
    # Games
    path('getGames/', views.getGames, name = 'getGames'),
    path('getGameById/<int:game_id>/', views.getGameById, name = 'getGameById'),
    path('createGame/', views.createGame, name = 'createGame'),
    path('modifyGame/<int:game_id>/', views.modifyGame, name = 'modifyGame'),
    path('deleteGame/<int:game_id>/', views.deleteGame, name = 'deleteGame'),
    # Genres
    path('getGenres/', views.getGenres, name = 'getGenres'),
    path('getGenreById/<int:genre_id>/', views.getGenreById, name = 'getGenreById'),
    path('createGenre/', views.createGenre, name = 'createGenre'),
    path('modifyGenre/<int:genre_id>/', views.modifyGenre, name = 'modifyGenre'),
    path('deleteGenre/<int:genre_id>/', views.deleteGenre, name = 'deleteGenre'),
    # # Playstore
    path('getPlaystoreGames/', views.getPlaystoreGames, name = 'getPlaystoreGames'),
    path('getPlaystoreGameByRow/<int:playstore_row>/', views.getPlaystoreGameByRow, name = 'getPlaystoreGameByRow'),
    path('addGameToPlaystore/', views.addGameToPlaystore, name = 'addGameToPlaystore'),
    path('modifyGameFromPlaystore/<int:playstore_row>/', views.modifyGameFromPlaystore, name = 'modifyGameFromPlaystore'),
    path('deleteGameFromPlaystore/<int:playstore_row>/', views.deleteGameFromPlaystore, name = 'deleteGameFromPlaystore'),
]
