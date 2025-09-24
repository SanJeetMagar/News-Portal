from rest_framework import generics, permissions
from .models import Author
from .serializers import AuthorSerializer, AuthorDetailSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = [permissions.AllowAny]

class AuthorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.author_profile
