from rest_framework import serializers
from .models import Article
from src.apps.authors.serializers import AuthorSerializer
from src.apps.interactions.models import Reaction, Comment
from src.apps.interactions.serializers import ReactionSerializer, CommentSerializer
from drf_spectacular.utils import extend_schema_field


class ArticleListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "slug", "excerpt", "category", "authors"]
        extra_kwargs = {
            "slug": {"read_only": True},
            "excerpt": {"required": False},
            "category": {"required": False},
            "authors": {"required": False},
        }


class ArticleDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    reactions = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {
            "slug": {"read_only": True},
            "excerpt": {"required": False},
            "category": {"required": False},
            "authors": {"required": False},
            "feature_image": {"required": False},
        }

    @extend_schema_field(serializers.ListSerializer(child=ReactionSerializer()))
    def get_reactions(self, obj):
        reactions = Reaction.objects.filter(article=obj)
        return ReactionSerializer(reactions, many=True).data

    @extend_schema_field(serializers.ListSerializer(child=CommentSerializer()))
    def get_comments(self, obj):
        comments = Comment.objects.filter(article=obj)
        return CommentSerializer(comments, many=True).data
