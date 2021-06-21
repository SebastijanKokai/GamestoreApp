from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from gamestore.models import Game, Genre, Playstore
from gamestore.serializers import GameSerializer, GenreSerializer, PlaystoreCreateSerializer, PlaystoreSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


# Create your views here.
    # # Home
    # path('', views.gamestore, name = 'gamestore'),
    # # Games
    # path('getGames/', views.gamestore, name = 'getGames'),
    # path('getGameById/<int:game_id>/', views.gamestore, name = 'getGameById'),
    # path('createGame/', views.gamestore, name = 'createGame'),
    # path('modifiyGame/<int:game_id>/', views.gamestore, name = 'modifiyGame'),
    # path('deleteGame/<int:game_id>/', views.gamestore, name = 'deleteGame'),
    # # Genres
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

def index():
    return JsonResponse("This is the home page.")

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def getGames(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_serializer = GameSerializer(games, many=True)
        return JsonResponse(game_serializer.data, safe=False)


