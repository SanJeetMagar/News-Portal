from django.urls import path
from .views import AuthorView, ArticleView, ArticleDetailView

urlpatterns = [
    # Authors
    path("authors/", AuthorView.as_view(), name="author-list-create"),

    # Articles
    path("articles/", ArticleView.as_view(), name="article-list-create"),
    path("articles/<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
]
