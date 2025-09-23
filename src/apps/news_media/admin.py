from django.contrib import admin
from .models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("title", "alt_txt")
    search_fields = ("title",)
    ordering = ("-created_at",)