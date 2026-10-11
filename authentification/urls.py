from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from .views import CurrentUserAPIView, LoginAPIView


app_name = "authentification"


urlpatterns = [
    path(
        "login/",
        LoginAPIView.as_view(),
        name="login",
    ),
    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="refresh",
    ),
    path(
        "verify/",
        TokenVerifyView.as_view(),
        name="verify",
    ),
    path(
        "me/",
        CurrentUserAPIView.as_view(),
        name="current-user",
    ),
]