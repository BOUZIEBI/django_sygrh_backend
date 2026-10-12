from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.models import Permission
from .models import Role, Agent

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = [
            "uid",
            "libelle",
            "code",
        ]


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = [
            "id",
            "codename",
            "name",
        ]



class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent

        fields = [
            "uid",
            "email",
            "nom",
            "prenoms",
            "matricule",
            "code",
            "date_naissance",
            "lieu_naissance",
            "telephone_principal",
            "telephone_secondaire",
            "email_professionnel",
            "email_personnel",
            "quartier",
            "nom_jeune_fille",
            "lieu_habitation",
            "date_recrutement",
            "date_depart",
            "nombre_enfant",
            "nom_prenoms_pere",
            "nom_prenoms_mere",
            "numero_piece_identite",
            "cree_le",
            "modifie_le",
            "preinscrit_le",
            "supprime_le",
            "date_premiere_prise_service_dans_structure",
            "date_premiere_prise_service_fonction_publique",

            # États
            "etat_handicap",
            "is_mode",
            "is_deleted",
            "est_preinscrit",

            # Relations avec les utilisateurs
            "cree_par",
            "modifie_par",
            "supprime_par",

            # Relations administratives
            "conjoint",
            "genre",
            "type_agent",
            "nationalite",
            "type_recrutement",
            "structure",
            "fonction",
            "situation_matrimoniale",
            "specialite",
            "situation_administrative",
            "grade",
            "statut",
            "user",
            "validation_fiche",
        ]

        read_only_fields = fields
        


class UserSerializer(serializers.ModelSerializer):

    role = RoleSerializer(
        read_only=True
    )

    permissions = serializers.SerializerMethodField()

    agent = AgentSerializer(
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = User

        fields = [
            "uid",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_verified",
            "role",
            "permissions",
            "agent",
            "cree_le",
            "modifie_le",
        ]

        read_only_fields = fields

    def get_permissions(self, obj):

        # Permissions directement attribuées à l'utilisateur
        permissions = obj.user_permissions.all()

        return PermissionSerializer(
            permissions,
            many=True
        ).data


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
        user.is_verified = True
        
        # Dates
        current_time = timezone.now()

        user.cree_le = current_time
        user.modifie_le = current_time

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