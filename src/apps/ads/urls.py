from django.urls import path
from .views import AdListView, AdCreateView, AdDetailView

urlpatterns = [
    path("", AdListView.as_view(), name="ad-list"),
    path("create/", AdCreateView.as_view(), name="ad-create"),
    path("<slug:slug>/", AdDetailView.as_view(), name="ad-detail"),
]
