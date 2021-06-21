from rest_framework import serializers
from gamestore.models import Game, Genre, Playstore

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('genreid',
        'genre')

class GameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    # gameid = serializers.IntegerField()

    class Meta:
        model = Game
        fields = ('gameid',
        'gamename',
        'datereleased',
        'gamedescription',
        'genres',
        'gameImgUrl')

class PlaystoreSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = Playstore
        fields = ('game',
        'gameprice',
        'discount',
        'dateadded')

class PlaystoreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playstore
        fields = ('game',
        'gameprice',
        'discount',
        'dateadded')