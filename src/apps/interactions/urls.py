from django.urls import path
from .views import (
    CommentListView,
    CommentDetailView,
    ReactionListCreateView,
)

urlpatterns = [
    # Comments
    path("comments/", CommentListView.as_view(), name="comment-list"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),

    # Article ko Reactions
    path("reactions/", ReactionListCreateView.as_view(), name="reaction-list-create"),
]
