from django.urls import path
from .views import (
    PublicArticleViewCountList,
    AuthorViewCountList,
    CategoryClickList,
)

urlpatterns = [
    path("articles/views/", PublicArticleViewCountList.as_view(), name="public-article-views"),
    path("authors/views/", AuthorViewCountList.as_view(), name="author-views"),
    path("categories/clicks/", CategoryClickList.as_view(), name="category-clicks"),
]
