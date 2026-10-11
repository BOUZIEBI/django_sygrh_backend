from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


class LoginSerializer(serializers.Serializer):
    print("LoginSerializer initialized")  # Debugging line
    identifiant = serializers.CharField(
        required=True,
        write_only=True,
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        trim_whitespace=False,
        style={"input_type": "password"},
    )
    print("LoginSerializer initialized with identifiant:", identifiant, "and password:", password)  # Debugging line
    def validate(self, attrs):
        identifiant = attrs.get("identifiant", "").strip()
        password = attrs.get("password", "")

        if not identifiant or not password:
            raise serializers.ValidationError(
                {
                    "message": (
                        "L'identifiant et le mot de passe "
                        "sont obligatoires."
                    ),
                }
            )

        # Recherche par username ou email
        user_found = (
            User.objects
            .filter(
                Q(username__iexact=identifiant)
                | Q(email__iexact=identifiant)
            )
            .first()
        )

        if user_found is None:
            raise serializers.ValidationError(
                {
                    "message": (
                        "Identifiant ou mot de passe incorrect."
                    ),
                }
            )

        user = authenticate(
            request=self.context.get("request"),
            username=user_found.get_username(),
            password=password,
        )

        if user is None:
            raise serializers.ValidationError(
                {
                    "message": (
                        "Identifiant ou mot de passe incorrect."
                    ),
                }
            )

        if not user.is_active:
            raise serializers.ValidationError(
                {
                    "message": (
                        "Ce compte utilisateur est désactivé."
                    ),
                }
            )

        refresh = RefreshToken.for_user(user)

        # Informations supplémentaires intégrées au JWT
        refresh["email"] = user.email
        refresh["username"] = user.get_username()
        refresh["is_superuser"] = user.is_superuser

        return {
            "user": user,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }