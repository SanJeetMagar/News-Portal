from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all().select_related("category").prefetch_related("authors")
    serializer_class = ArticleListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all().select_related("category").prefetch_related("authors")
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]
