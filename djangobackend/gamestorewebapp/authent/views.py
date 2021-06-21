from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from gamestore.models import AuthUser, Gamelibrary, Wishlist, Friendlist
from authent.serializers import FriendlistSerializer, WishlistSerializer, FriendlistGetSerializer, WishlistGetSerializer, GameLibrarySerializer, GameLibraryGetSerializer, RegistrationSerializer, MyTokenObtainPairSerializer, AuthUserSerializer, AuthUserGetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST',])
def registration(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    if request.method == 'GET':
        users = AuthUser.objects.all()
        user_serializer = AuthUserGetSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserById(request, user_id):
    try:
        user = AuthUser.objects.get(id=user_id)
    except AuthUser.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        user_serializer = AuthUserGetSerializer(user)
        return JsonResponse(user_serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def modifyUser(request, user_id):
    if request.method == 'PUT':
        try:
            user = AuthUser.objects.get(id=user_id)
        except AuthUser.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        user_data = JSONParser().parse(request)
        user_serializer = AuthUserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, user_id):
    try:
        user = AuthUser.objects.get(id=user_id)
    except AuthUser.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getLibraries(request):
    if request.method == 'GET':
        gamelibrary = Gamelibrary.objects.all()
        gamelibrary_serializer = GameLibrarySerializer(gamelibrary, many=True)
        return JsonResponse(gamelibrary_serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLibraryByUser(request):
    if request.method == 'GET':
        gamelibraries = Gamelibrary.objects.filter(userid=request.user.id)
        gamelibrary_serializer = GameLibraryGetSerializer(gamelibraries, many=True)
        return JsonResponse(gamelibrary_serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createLibraryRow(request):
    if request.method == 'POST':
        userid = request.user.id
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        gameid = body['gameid']
        gamelibrary_serializer = GameLibrarySerializer(data={"userid": userid, "game": gameid, "totaltimeplayed": 0})
        if gamelibrary_serializer.is_valid():
            gamelibrary_serializer.save()
            return JsonResponse(gamelibrary_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(gamelibrary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteLibraryRow(request, game_id):
    try:
        game = Gamelibrary.objects.filter(game=game_id)
        user_game = game.filter(userid=request.user.id)
    except Gamelibrary.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist in the game library'}, status=status.HTTP_404_NOT_FOUND)
    if user_game is None:
       return JsonResponse({'message': 'The game does not exist in the game library'}, status=status.HTTP_404_NOT_FOUND) 
    elif request.method == 'DELETE':
        user_game.delete()
        return JsonResponse({'message': 'Game was deleted successfully from the game library.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWishlistByUser(request):
    if request.method == 'GET':
        wishlist = Wishlist.objects.filter(userid=request.user.id)
        wishlist_serializer = WishlistGetSerializer(wishlist, many=True)
        return JsonResponse(wishlist_serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createWishlistRow(request):
    if request.method == 'POST':
        userid = request.user.id
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        gameid = body['gameid']
        wishlist_serializer = WishlistSerializer(data={"userid": userid, "game": gameid})
        if wishlist_serializer.is_valid():
            wishlist_serializer.save()
            return JsonResponse(wishlist_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(wishlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteWishlistRow(request, game_id):
    try:
        game = Wishlist.objects.filter(game=game_id)
        user_game = game.filter(userid=request.user.id)
    except Gamelibrary.DoesNotExist:
        return JsonResponse({'message': 'The game does not exist in the wish list'}, status=status.HTTP_404_NOT_FOUND)
    if user_game is None:
       return JsonResponse({'message': 'The game does not exist in the wish list'}, status=status.HTTP_404_NOT_FOUND) 
    elif request.method == 'DELETE':
        user_game.delete()
        return JsonResponse({'message': 'Game was deleted successfully from the wish list.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFriendlistByUser(request):
    if request.method == 'GET':
        friendlist = Friendlist.objects.filter(user=request.user.id)
        friendlist_serializer = FriendlistGetSerializer(friendlist, many=True)
        return JsonResponse(friendlist_serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createFriendlistRow(request):
    if request.method == 'POST':
        userid = request.user.id
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        friendid = body['friendid']
        friendlist_serializer = FriendlistSerializer(data={"user": userid, "friend": friendid})
        if friendlist_serializer.is_valid():
            friendlist_serializer.save()
            return JsonResponse(friendlist_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(friendlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteFriendlistRow(request, friend_id):
    try:
        friend = Friendlist.objects.filter(friend=friend_id)
        user_friend = friend.filter(user=request.user.id)
        # Reverse delete also
        # user = Friendlist.objects.filter(friend=request.user.id)
        # friend_user = user.filter(user=friend.id)
    except Friendlist.DoesNotExist:
        return JsonResponse({'message': 'The friend does not exist in the friend list'}, status=status.HTTP_404_NOT_FOUND)
    if user_friend is None:
       return JsonResponse({'message': 'The friend does not exist in the friend list'}, status=status.HTTP_404_NOT_FOUND) 
    elif request.method == 'DELETE':
        user_friend.delete()
        # friend_user.delete()
        return JsonResponse({'message': 'Friend was deleted successfully from the friend list.'}, status=status.HTTP_204_NO_CONTENT)





