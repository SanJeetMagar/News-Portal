from rest_framework import serializers
from .models import Author, Article

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


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {
            'slug' : {'read_only':True},
            'excerpt': {'required': False},
            'category':{'required': False},
            'authors': {'required': False},
            'feature_image':{'required': False},
                   
        }

#