from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "titre",
            "description",
            "date_publication",
            "est_actif",
        ]
        read_only_fields = [
            "id",
            "date_publication",
        ]