from src.apps.common.models import TimestampModel
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Media(TimestampModel):
    FILE_TYPES = (
        ("image","Image"),
        ("video","Video"),
        ("audio", "Audio"),
        ("document", "Document")
    )
    file = models.FileField(upload_to="uploads/")
    title = models.CharField(max_length=255, null= True, blank= True)
    alt_txt = models.CharField(max_length=255, blank=True, null= True)
    file_type = models.CharField(max_length=20,choices=FILE_TYPES,default="image")


    def __str__(self) -> str:
        return self.title if self.title else str(self.file)