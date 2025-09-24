from django.db import models
from src.apps.common.models import TimestampModel
from src.apps.common.utils import generate_unique_slug
from src.apps.authors.models import Author
from src.apps.categories.models import Category


class Article(TimestampModel):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name="articles")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles",
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    feature_image = models.ImageField(upload_to="articles/", null=True, blank=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)
