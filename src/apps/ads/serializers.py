from rest_framework import serializers
from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    advertiser = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ad
        fields = "__all__"
        extra_kwargs = {
            "slug": {"read_only": True},
            "advertiser": {"read_only": True},
            "category": {"required": False},
            "link": {"required": False},
        }
