from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from src.apps.analytics.models import ArticleView  #view here implies analytics not the article view, I know confusing name, but too lazy to change now


class ArticleView(ListAPIView):
    queryset = Article.objects.filter(status="published") 
    serializer_class = ArticleListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        article = self.get_object()
        ArticleView.objects.create(
            article=article,
            user=request.user if request.user.is_authenticated else None,
            ip_address=request.META.get("REMOTE_ADDR"),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )
        return response
