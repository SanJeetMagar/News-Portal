from django.urls import path
from .views import ArticleView, ArticleDetailView

urlpatterns = [
    path("articles/", ArticleView.as_view(), name="article-list"),
    path("articles/<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
]
