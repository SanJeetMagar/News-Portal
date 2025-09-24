from django.db import models
from src.apps.common.models import TimestampModel
from src.apps.common.utils import generate_unique_slug


class Category(TimestampModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)
