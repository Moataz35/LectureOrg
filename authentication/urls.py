from django.urls import path
from .views import UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', UserCreateAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
