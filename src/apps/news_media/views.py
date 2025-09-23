from django.shortcuts import render
from .serializers import MediaSerializer
from .models import Media
from rest_framework import viewsets

class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
