from rest_framework import serializers
from gamestore.models import Game, Genre, Playstore

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('genreid',
        'genre')

class GameSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    gameid = serializers.IntegerField()

    class Meta:
        model = Game
        fields = ('gameid',
        'gamename',
        'datereleased',
        'gamedescription',
        'genres')

class PlaystoreSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True, many=True)

    class Meta:
        model = Playstore
        fields = ('game',
        'gameprice',
        'discount',
        'dateadded')

    def create(self, validated_data):
        game_data = validated_data.pop('game')
        playstore = Playstore.objects.create(**validated_data)
        for data in game_data:
            Game.objects.create(game=game, **data)
        return playstore
