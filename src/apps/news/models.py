from django.db import models
from src.apps.common.models import TimestampModel
from src.apps.common.utils import generate_unique_slug
from src.apps.auth.models import User


class Author(TimestampModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="author", null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to="authors", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)


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



# class Media(TimestampModel):
