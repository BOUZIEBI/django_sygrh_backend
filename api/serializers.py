from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    role_uid = serializers.UUIDField(
        source="role_id",
        read_only=True
    )

    class Meta:
        model = User
        fields = [
            "uid",
            "username",
            "email",
            "role_uid",
            "is_verified",
            "is_active",
            "is_superuser",
            "cree_le",
        ]
        read_only_fields = fields


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password_confirm = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User

        fields = [
            "uid",
            "username",
            "email",
            "password",
            "password_confirm",
        ]

        read_only_fields = ["uid"]

    def validate(self, attrs):

        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({
                "password_confirm": "Les mots de passe ne correspondent pas."
            })

        return attrs

    def validate_email(self, value):

        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "Cette adresse email est déjà utilisée."
            )

        return value

    def create(self, validated_data):

        validated_data.pop("password_confirm")

        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        # À adapter selon ton processus d'activation.
        user.is_active = True
        user.is_verified = False

        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True
    )


class LogoutSerializer(serializers.Serializer):

    refresh_token = serializers.CharField(
        required=True
    )