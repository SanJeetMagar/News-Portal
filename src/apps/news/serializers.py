from rest_framework import serializers
from .models import Author, Article
from src.apps.interactions.models import Reaction, Comment
from src.apps.interactions.serializers import ReactionSerializer, CommentSerializer
from drf_spectacular.utils import extend_schema_field
class AuthorSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Author
        fields = "__all__"
        extra_kwargs = {
            'slug': {'read_only': True},
            'bio': {'required':False},
            'profile_image': {'required': False},
            'email': {'required': False},
            'designation': {'required':False},
            'facebook': {"required": False},
            'twitter': {'required': False},
            "instagram" :{'required': False},
            "linkedin": {'required':False},
        }
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "slug", "excerpt", "category", "authors"]
        extra_kwargs = {
            'slug': {'read_only': True},
            'excerpt': {'required': False},
            'category': {'required': False},
            'authors': {'required': False},
            # 'feature_image': {'required': False},
            
        }

class ArticleDetailSerializer(serializers.ModelSerializer):
    reactions = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    authors = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {
            'slug': {'read_only': True},
            'excerpt': {'required': False},
            'category': {'required': False},
            'authors': {'required': False},
            'feature_image': {'required': False},
            
        }
    @extend_schema_field(serializers.ListSerializer(child=ReactionSerializer()))
    def get_reactions(self, obj):
        reactions = Reaction.objects.filter(article=obj)
        return ReactionSerializer(reactions, many=True).data

    @extend_schema_field(serializers.ListSerializer(child=CommentSerializer()))
    def get_comments(self, obj):
        comments = Comment.objects.filter(article=obj)
        return CommentSerializer(comments, many=True).data
