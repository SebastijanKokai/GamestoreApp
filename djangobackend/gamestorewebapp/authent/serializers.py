from gamestore.models import AuthUser, Gamelibrary, Wishlist, Friendlist
from gamestore.serializers import GameSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=AuthUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AuthUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'phone_number', 'nickname')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'nickname': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def save(self):
        user = AuthUser.objects.create(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            phone_number = self.validated_data['phone_number'],
            nickname = self.validated_data['nickname']
        )
        user.set_password(self.validated_data['password'])
        user.save()

        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        token['is_active'] = user.is_active
        return token

class AuthUserGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'first_name', 'last_name', 'nickname',
        'user_level', 'date_joined')

class AuthUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuthUser
        fields = ('id',
        'username',
        'nickname',
        'user_level',
        'is_staff')

class GameLibrarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gamelibrary
        fields = ('game', 'userid', 'totaltimeplayed', 'lasttimeplayed')

class GameLibraryGetSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = Gamelibrary
        fields = ('game', 'userid', 'totaltimeplayed', 'lasttimeplayed')

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = ('game', 'userid')


class WishlistGetSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = ('game', 'userid')

class FriendlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friendlist
        fields = ('user', 'friend')

class FriendlistGetSerializer(serializers.ModelSerializer):
    user = AuthUserGetSerializer(read_only=True)
    friend = AuthUserGetSerializer(read_only=True)

    class Meta:
        model = Friendlist
        fields = ('user', 'friend')