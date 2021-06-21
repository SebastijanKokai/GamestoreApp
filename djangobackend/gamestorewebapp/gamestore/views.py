from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from gamestore.models import Game, Genre, Playstore
from gamestore.serializers import GameSerializer, GenreSerializer, PlaystoreCreateSerializer, PlaystoreSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.parsers import JSONParser


def index():
    return JsonResponse("This is the home page.")

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def getGames(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_serializer = GameSerializer(games, many=True)
        return JsonResponse(game_serializer.data, safe=False)

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def getGameById(request, game_id):
    try:
        game = Game.objects.get(gameid=game_id)
    except Game.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return JsonResponse(game_serializer.data)

@api_view(['POST'])
# @permission_classes([IsAdminUser])
def createGame(request):
    if request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def modifyGame(request, game_id):
    try:
        game = Game.objects.get(gameid=game_id)
    except Game.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(game, data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deleteGame(request, game_id):
    try:
        game = Game.objects.get(gameid=game_id)
    except Game.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        game.delete()
        return JsonResponse({'message': 'Game was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def getGenres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        genre_serializer = GenreSerializer(genres, many=True)
        return JsonResponse(genre_serializer.data, safe=False)

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def getGenreById(request, genre_id):
    try:
        genre = Genre.objects.get(genreid=genre_id)
    except Genre.DoesNotExist:
        return JsonResponse({'message': 'The genre does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        genre_serializer = GenreSerializer(genre)
        return JsonResponse(genre_serializer.data)

@api_view(['POST'])
# @permission_classes([IsAdminUser])
def createGenre(request):
    if request.method == 'POST':
        genre_data = JSONParser().parse(request)
        genre_serializer = GenreSerializer(data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse(genre_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def modifyGenre(request, genre_id):
    try:
        genre = Genre.objects.get(genreid=genre_id)
    except Genre.DoesNotExist:
        return JsonResponse({'message': 'The genre does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        genre_data = JSONParser().parse(request)
        genre_serializer = GenreSerializer(genre, data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse(genre_serializer.data)
        return JsonResponse(genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deleteGenre(request, genre_id):
    try:
        genre = Genre.objects.get(genreid=genre_id)
    except Genre.DoesNotExist:
        return JsonResponse({'message': 'The genre does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Genre was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getPlaystoreGames(request):
    if request.method == 'GET':
        playstore = Playstore.objects.all()
        playstore_serializer = PlaystoreSerializer(playstore, many=True)
        return JsonResponse(playstore_serializer.data, safe=False)

@api_view(['GET'])
def getPlaystoreGameByRow(request, playstore_row):
    try:
        playstorerow = Playstore.objects.get(playstorerow=playstore_row)
    except Playstore.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist in the playstore'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        playstore_serializer = PlaystoreSerializer(playstorerow)
        return JsonResponse(playstore_serializer.data)

@api_view(['POST'])
# @permission_classes([IsAdminUser])
def addGameToPlaystore(request):
    if request.method == 'POST':
        gamestore_data = JSONParser().parse(request)
        playstore_serializer = PlaystoreCreateSerializer(data = gamestore_data)
        if playstore_serializer.is_valid():
            playstore_serializer.save()
            return JsonResponse(playstore_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(playstore_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def modifyGameFromPlaystore(request, playstore_row):
    try:
        playstorerow = Playstore.objects.get(playstorerow=playstore_row)
    except Playstore.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist in the playstore'}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        playstore_data = JSONParser().parse(request)
        playstore_serializer = PlaystoreCreateSerializer(playstorerow, data=playstore_data)
        if playstore_serializer.is_valid():
            playstore_serializer.save()
            return JsonResponse(playstore_serializer.data)
        return JsonResponse(playstore_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deleteGameFromPlaystore(request, playstore_row):
    try:
        playstorerow = Playstore.objects.get(playstorerow=playstore_row)
    except Playstore.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist in the playstore'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        playstorerow.delete()
        return JsonResponse({'message': 'Game was deleted successfully from the playstore.'}, status=status.HTTP_204_NO_CONTENT)


