from django.urls import path
from gamestore.views import getGames, index
from . import views

app_name = 'gamestore'


urlpatterns = [
    # Home
    path('', views.index, name = 'index'),
    # Games
    path('getGames/', getGames, name = 'getGames'),
    path('getGameById/<int:game_id>/', views.index, name = 'getGameById'),
    path('createGame/', views.index, name = 'createGame'),
    path('modifiyGame/<int:game_id>/', views.index, name = 'modifiyGame'),
    path('deleteGame/<int:game_id>/', views.index, name = 'deleteGame'),
    # Genres
    # path('getGenres/', views.gamestore, name = 'getGenres'),
    # path('getGenreById/<int:genre_id>/', views.gamestore, name = 'getGenreById'),
    # path('createGenre/', views.gamestore, name = 'createGenre'),
    # path('modifyGenre/<int:genre_id>/', views.gamestore, name = 'modifyGenre'),
    # path('deleteGenre/<int:genre_id>/', views.gamestore, name = 'deleteGenre'),
    # # Playstore
    # path('getPlaystoreGames/', views.gamestore, name = 'getPlaystoreGames'),
    # path('addGameToPlaystore/<int:game_id>/', views.gamestore, name = 'addGameToPlaystore'),
    # path('deleteGameFromPlaystore/<int:game_id>/', views.gamestore, name = 'deleteGameFromPlaystore'),
    # path('modifyGameFromPlaystore/<int:game_id>/', views.gamestore, name = 'modifyGameFromPlaystore'),
]
