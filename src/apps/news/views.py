from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import ListCreateAPIView


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer
