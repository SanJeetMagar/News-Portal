from django.urls import path, include
from .views import AuthorView

urlpatterns = [
    path("author/",AuthorView.as_view(), name="Author"),
    
]