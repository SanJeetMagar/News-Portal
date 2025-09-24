from django.db import models
from django.utils.text import slugify
from src.apps.common.models import TimestampModel
from src.apps.auth.models import User
from src.apps.categories.models import Category

class AdType(models.TextChoices):
    GENERAL = "general", "General"
    CATEGORY = "category", "Category"


class AdPlacement(models.TextChoices):
    HOMEPAGE = "homepage", "Homepage"
    SIDEBAR = "sidebar", "Sidebar"
    ARTICLE_TOP = "article_top", "Article Top"
    ARTICLE_MIDDLE = "article_middle", "Article Middle"
    ARTICLE_BOTTOM = "article_bottom", "Article Bottom"
    POPUP = "popup", "Popup"


class Ad(TimestampModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to="ads/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    ad_type = models.CharField(
        max_length=20, choices=AdType.choices, default=AdType.GENERAL
    )
    placement = models.CharField(
        max_length=50, choices=AdPlacement.choices, default=AdPlacement.SIDEBAR
    )

    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="ads",
        null=True,
        blank=True,
    )

    advertiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ads"
    )

    is_active = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def is_currently_active(self):
        """
        Returns True if the ad is active and within its start/end date range.
        """
        from django.utils.timezone import now
        today = now().date()

        if not self.is_active:
            return False
        if self.start_date and today < self.start_date:
            return False
        if self.end_date and today > self.end_date:
            return False
        return True

    def __str__(self):
        return f"{self.title} ({self.get_ad_type_display()})"
