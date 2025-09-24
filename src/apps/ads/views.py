from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.timezone import now
from .models import Ad
from .serializers import AdSerializer
from src.apps.common.permissions import (
    IsAdminOrSuperAdmin,
    IsAdvertiser,
    IsOwnerOrAdmin,
)

from src.apps.ads import models


class AdListView(ListAPIView):
    queryset = Ad.objects.all()

    serializer_class = AdSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Ad.objects.filter(is_active=True)
        today = now().date()
        queryset = queryset.filter(
            models.Q(start_date__isnull=True) | models.Q(start_date__lte=today),
            models.Q(end_date__isnull=True) | models.Q(end_date__gte=today),
        )
        placement = self.request.query_params.get("placement")
        category_id = self.request.query_params.get("category")

        if placement:
            queryset = queryset.filter(placement=placement)

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated & (IsAdminOrSuperAdmin | IsAdvertiser)]

    def perform_create(self, serializer):
        serializer.save(advertiser=self.request.user)


class AdDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny] 

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), (IsOwnerOrAdmin())]
        return [AllowAny()]
