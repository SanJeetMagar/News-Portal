from rest_framework import generics
from src.apps.common.permissions import IsAuthor
from .models import Article
from .serializers import ArticleWriteSerializer


class AuthorArticleListView(generics.ListCreateAPIView):
    """
    List all articles written by the logged-in author
    and allow them to create new ones.
    """
    serializer_class = ArticleWriteSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Article.objects.filter(authors__user=self.request.user)

    def perform_create(self, serializer):
        # Save the article and assign the logged-in user as the author
        article = serializer.save()
        article.authors.add(self.request.user.author_profile)
        article.save()


class AuthorArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific article
    belonging to the logged-in author.
    """
    serializer_class = ArticleWriteSerializer
    permission_classes = [IsAuthor]
    lookup_field = "slug"

    def get_queryset(self):
        return Article.objects.filter(authors__user=self.request.user)
