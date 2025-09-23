from rest_framework import serializers
from .models import Comment, Reaction, CommentReaction
from drf_spectacular.utils import extend_schema_field

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()
    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "article",
            "parent",
            "content",
            "is_approved",
            "created_at",
            "updated_at",
            "replies",
            "reactions",
        ]
        read_only_fields = ["user", "created_at", "updated_at"]
   
    @extend_schema_field(serializers.ListSerializer(child=serializers.DictField()))
    def get_replies(self, obj):
        # Nested replies
        return CommentSerializer(obj.replies.all(), many=True).data

    @extend_schema_field(serializers.DictField(
        child=serializers.IntegerField()
    ))
    def get_reactions(self, obj):
        # Returns count of each reaction type
        return {
            reaction_type: obj.comment_reactions.filter(reaction_type=reaction_type).count()
            for reaction_type, _ in CommentReaction.REACTIONS
        }

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["user"] = request.user
        return super().create(validated_data)


class ReactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reaction
        fields = ["id", "user", "article", "reaction_type", "created_at", "updated_at"]
        read_only_fields = ["user", "created_at", "updated_at"]

    @extend_schema_field(serializers.DictField())
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["user"] = request.user
        return super().create(validated_data)


class CommentReactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CommentReaction
        fields = ["id", "user", "comment", "reaction_type", "created_at", "updated_at"]
        read_only_fields = ["user", "created_at", "updated_at"]

    @extend_schema_field(serializers.DictField())
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["user"] = request.user
        return super().create(validated_data)
