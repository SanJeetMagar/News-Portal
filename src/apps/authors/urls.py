from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorUpdateView

urlpatterns = [
    path("", AuthorListView.as_view(), name="author-list"),
    path("<slug:slug>/", AuthorDetailView.as_view(), name="author-detail"),
    path("me/update/", AuthorUpdateView.as_view(), name="author-update"),
]
