from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    LogoutView,
    UserProfileView,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("logout/", LogoutView.as_view(), name="user-logout"),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
]