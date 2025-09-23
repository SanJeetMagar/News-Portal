from django.contrib import admin

from .models import Comment, Reaction, CommentReaction


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "article", "parent", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at", "updated_at")
    search_fields = ("user__username", "article__title", "content")
    readonly_fields = ("created_at", "updated_at")
    actions = ["approve_comments", "disapprove_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected comments have been approved.")

    def disapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, "Selected comments have been disapproved.")
    approve_comments.short_description = "Approve selected comments"
    disapprove_comments.short_description = "Disapprove selected comments"
@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "article", "reaction_type", "created_at")
    list_filter = ("reaction_type", "created_at", "updated_at")
    search_fields = ("user__username", "article__title")
    readonly_fields = ("created_at", "updated_at")
@admin.register(CommentReaction)
class CommentReactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "comment", "reaction_type", "created_at")
    list_filter = ("reaction_type", "created_at", "updated_at")
    search_fields = ("user__username", "comment__content")
    readonly_fields = ("created_at", "updated_at")  
