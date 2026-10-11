from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    print("LoginAPIView initialized")  # Debugging line
    def post(self, request):
        serializer = LoginSerializer(
            data=request.data,
            context={
                "request": request,
            },
        )
        
        if not serializer.is_valid():
            return Response(
                {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "message": "Échec de la connexion.",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.validated_data["user"]
        access_token = serializer.validated_data[
            "access_token"
        ]
        refresh_token = serializer.validated_data[
            "refresh_token"
        ]

        expires_in = int(
            settings
            .SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]
            .total_seconds()
        )

        return Response(
            {
                "code": status.HTTP_200_OK,
                "success": True,
                "message": "Connexion effectuée avec succès.",
                "data": {
                    "token_type": "Bearer",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "expires_in": expires_in,
                    "user": {
                        "id": user.pk,
                        "username": user.get_username(),
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "is_staff": user.is_staff,
                        "is_superuser": user.is_superuser,
                    },
                },
            },
            status=status.HTTP_200_OK,
        )


class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response(
            {
                "code": status.HTTP_200_OK,
                "success": True,
                "message": "Utilisateur récupéré avec succès.",
                "data": {
                    "id": user.pk,
                    "username": user.get_username(),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                },
            },
            status=status.HTTP_200_OK,
        )