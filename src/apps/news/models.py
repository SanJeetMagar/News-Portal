from django.db import models
from src.apps.common.models import TimestampModel
from src.apps.common.utils import generate_slug
class Author(TimestampModel):
    name = models.CharField(max_length=100) 
    slug = models.SlugField(unique=True, null=True, blank=True)
    bio = models.TextField(blank= True, null=True)
    profile_image = models.ImageField(upload_to= 'authors', blank= True, null= True)
    email = models.EmailField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null= True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Author"
        verbose_name_plural =  "Authors"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = generate_slug(self.name)
            super().save(*args, **kwargs)
