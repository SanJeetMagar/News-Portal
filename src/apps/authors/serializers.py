from rest_framework import serializers
from .models import Author
from src.apps.articles.models import Article
from drf_spectacular.utils import extend_schema_field
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id", "user", "name", "slug", "bio", "profile_image", 
            "designation", "facebook", "twitter", "instagram", "linkedin"
        ]
        read_only_fields = ["user", "slug"]

class AuthorDetailSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = [
            "id", "user", "name", "slug", "bio", "profile_image",
            "designation", "facebook", "twitter", "instagram", "linkedin", "articles"
        ]
    @extend_schema_field(serializers.ListSerializer(
        child=serializers.DictField()
    ))
    def get_articles(self, obj):
        return [{"id": a.id, "title": a.title, "status": a.status} for a in obj.articles.all()]

class BaseAuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = [
            "id","name", "slug"
        ]