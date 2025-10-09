from rest_framework import serializers
from .models import ArticleView, CategoryClick
from src.apps.articles.models import Article
from src.apps.authors.models import Author
from django.db.models import Count


class ArticleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleView
        fields = ["id", "article", "user", "ip_address", "user_agent", "created_at"]


class CategoryClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryClick
        fields = ["id", "category", "user", "created_at"]


class ArticleViewCountSerializer(serializers.ModelSerializer):
    views_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ["id", "title", "views_count"]


class AuthorViewCountSerializer(serializers.ModelSerializer):
    total_views = serializers.IntegerField()

    class Meta:
        model = Author
        fields = ["id", "name", "total_views"]