from django.db import models
from django.conf import settings
from src.apps.common.models import TimestampModel
from src.apps.articles.models import Article
from src.apps.categories.models import Category

User = settings.AUTH_USER_MODEL

class ArticleView(TimestampModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="views")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"View: {self.article.title} by {self.user or self.ip_address}"


class CategoryClick(TimestampModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="clicks")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Click: {self.category.name} by {self.user or 'Anonymous'}"
