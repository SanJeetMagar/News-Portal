from .models import Author, Article
from .serializers import ArticleListSerializer, AuthorSerializer , ArticleDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer

class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all().select_related('authors')
    serializer_class = ArticleListSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all().prefetch_related('reactions', 'comments').select_related('authors')
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"