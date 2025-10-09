from django.urls import path, include
from .views import ArticleView, ArticleDetailView
from .author_views import AuthorArticleDetailView, AuthorArticleListView
urlpatterns = [
    path("", ArticleView.as_view(), name="article-list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("author/", AuthorArticleListView.as_view(), name="author-article-list"),
    path("author/<slug:slug>/", AuthorArticleDetailView.as_view(), name="author-article-detail"),
]