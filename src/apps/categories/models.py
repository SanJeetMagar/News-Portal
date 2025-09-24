from django.db import models
from src.apps.common.models import TimestampModel
from src.apps.common.utils import generate_unique_slug




class Category(TimestampModel):
    name = models.CharField(max_length=100, unique=True, default="Uncategorized")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

