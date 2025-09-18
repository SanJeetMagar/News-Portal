from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
def get_login_response(user):
    refresh = RefreshToken.for_user(user)
    return {
        "msg": "Login successful",
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "details": UserSerializer(user).data
    }