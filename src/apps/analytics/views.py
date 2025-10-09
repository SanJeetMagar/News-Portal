from rest_framework import generics
from django.db.models import Count
from .models import CategoryClick
from .serializers import ArticleViewCountSerializer, AuthorViewCountSerializer, CategoryClickSerializer
from src.apps.articles.models import Article
from src.apps.authors.models import Author
from src.apps.common import permissions

class PublicArticleViewCountList(generics.ListAPIView):
    queryset = Article.objects.annotate(views_count=Count("views"))
    serializer_class = ArticleViewCountSerializer


class AuthorViewCountList(generics.ListAPIView):
    serializer_class = AuthorViewCountSerializer


    def get_queryset(self):
        qs = Author.objects.annotate(total_views=Count("articles__views"))
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return qs
        return qs.filter(user=user) 


class CategoryClickList(generics.ListAPIView):
    queryset = CategoryClick.objects.all()
    serializer_class = CategoryClickSerializer
