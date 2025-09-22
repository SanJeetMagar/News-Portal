from django.contrib import admin
from .models import Author, Category, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "designation", "slug")
    search_fields = ("name", "email", "designation")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "category", "slug", "created_at")
    search_fields = ("title", "content", "excerpt")
    list_filter = ("status", "category", "authors")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("authors",)
    ordering = ("-created_at",)

    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "slug", "excerpt", "status"),
        }),
        ("Content", {
            "fields": ("content", "feature_image"),
        }),
        ("Relations", {
            "fields": ("authors", "category"),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
        }),
    )

    readonly_fields = ("created_at", "updated_at")
