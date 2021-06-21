from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'authent'

urlpatterns = [
    # Register, Login, Custom Token with claims
    path('register/', views.registration, name="register"),
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # User
    path('getUsers/', views.getUsers, name="getUsers"),
    path('getUserById/<int:user_id>/', views.getUserById, name="getUserById"),
    path('modifyUser/<int:user_id>/', views.modifyUser, name="modifyUser"),
    path('deleteUser/<int:user_id>/', views.deleteUser, name="deleteUser"),
    # Game library
    path('getLibraryByUser/', views.getLibraryByUser, name="getLibraryByUser"),
    path('getLibraries/', views.getLibraries, name="getLibraries"),
    path('createLibraryRow/', views.createLibraryRow, name="createLibraryRow"),
    path('deleteLibraryRow/<int:game_id>/', views.deleteLibraryRow, name="deleteLibraryRow"),
    # Wish List
    path('getWishlistByUser/', views.getWishlistByUser, name="getWishlistByUser"),
    path('createWishlistRow/', views.createWishlistRow, name="createWishlistRow"),
    path('deleteWishlistRow/<int:game_id>/', views.deleteWishlistRow, name="deleteWishlistRow"),
    # Friend List
    path('getFriendlistByUser/', views.getFriendlistByUser, name="getFriendlistByUser"),
    path('createFriendlistRow/', views.createFriendlistRow, name="createFriendlistRow"),
    path('deleteFriendlistRow/<int:friend_id>/', views.deleteFriendlistRow, name="deleteFriendlistRow"),
]