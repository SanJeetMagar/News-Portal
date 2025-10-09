from rest_framework import serializers

from src.apps.authors.models import Author
from .models import Article
from src.apps.authors.serializers import AuthorSerializer, BaseAuthorSerializers
from src.apps.interactions.models import Reaction, Comment
from src.apps.interactions.serializers import ReactionSerializer, CommentSerializer
from drf_spectacular.utils import extend_schema_field


class ArticleListSerializer(serializers.ModelSerializer):
    authors = BaseAuthorSerializers(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "slug", "excerpt", "category", "authors"]
       
class ArticleDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    reactions = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()
    

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ["slug", "created_at", "updated_at", "views_count", ]
        

    @extend_schema_field(serializers.ListSerializer(child=ReactionSerializer()))
    def get_reactions(self, obj):
        reactions = Reaction.objects.filter(article=obj)
        return ReactionSerializer(reactions, many=True).data

    @extend_schema_field(serializers.ListSerializer(child=CommentSerializer()))
    def get_comments(self, obj):
        comments = Comment.objects.filter(article=obj)
        return CommentSerializer(comments, many=True).data

    @extend_schema_field(serializers.IntegerField())
    def get_views_count(self, obj):
        return obj.views.count()

class ArticleWriteSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        many=True,
        slug_field="slug",
        queryset=Author.objects.all(),
        required=False,
    )

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "category",
            "status",
            "authors",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]
