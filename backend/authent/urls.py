from authent.views import registration_view, testview, MyObtainTokenPairView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'backend'

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', testview, name="testview"),

]