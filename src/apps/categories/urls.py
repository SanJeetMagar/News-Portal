from django.urls import path
from .views import CategoryView, CategoryDetailView

urlpatterns = [
    path("categories/", CategoryView.as_view(), name="category-list"),
    path("categories/<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"),
]
