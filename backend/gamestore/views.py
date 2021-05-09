from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from gamestore.models import Game, Gamegenre, Genre, Playstore
from gamestore.serializers import GameSerializer, GenreSerializer, PlaystoreSerializer
from rest_framework.decorators import api_view

from django.http import HttpResponse, Http404
from django.template import loader

import logging
from django.core import serializers

@api_view(['GET', 'POST', 'DELETE'])
def gamestore(request):
    if request.method == 'GET':
        playstore = Playstore.objects.all()
        playstore_serializer = PlaystoreSerializer(playstore, many=True)
        return JsonResponse(playstore_serializer.data, safe=False)

    elif request.method == 'POST':
        gamestore_data = JSONParser().parse(request)
        # game_data = Game.objects.get(gameid=)
        playstore_serializer = PlaystoreSerializer(data = gamestore_data)
        if playstore_serializer.is_valid():
            playstore_serializer.save()
            return JsonResponse(playstore_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(playstore_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST', 'DELETE'])
def games(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return JsonResponse(games_serializer.data, safe=False)

    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Game.objects.all().delete()
        return JsonResponse({'message': 'Games were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def game(request, game_id):
    # find game by id
    try:
        game = Game.objects.get(gameid=game_id)
    except Game.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return JsonResponse(game_serializer.data)

    elif request.method == 'PUT':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(game, data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return JsonResponse({'message': 'Game was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def genres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        genre_serializer = GenreSerializer(genres, many=True)
        return JsonResponse(genre_serializer.data, safe=False)

    elif request.method == 'POST':
        genre_data = JSONParser().parse(request)
        genre_serializer = GenreSerializer(data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse(genre_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Genre.objects.all().delete()
        return JsonResponse({'message': 'Genres were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def genre(request, genre_id):
    try:
        genre = Genre.objects.get(genreid=genre_id)
    except Genre.DoesNotExist:
        return JsonResponse({'message': 'The genre does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        genre_serializer = GenreSerializer(genre)
        return JsonResponse(genre_serializer.data)

    elif request.method == 'PUT':
        genre_data = JSONParser().parse(request)
        genre_serializer = GenreSerializer(genre, data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse(genre_serializer.data)
        return JsonResponse(genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Genre was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
