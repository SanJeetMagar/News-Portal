import os
import re
from django.core.exceptions import ValidationError
from django.utils.text import slugify


def image_validate(image):
    """
    Validate uploaded images to ensure size and extension.
    """
    allowed_exts = (".jpg", ".jpeg", ".png")
    file_extension = os.path.splitext(str(image))[1].lower()

    if image.size >= 1_000_000:  # 1MB
        raise ValidationError("File size must be less than 1MB")

    if file_extension not in allowed_exts:
        raise ValidationError("Only JPEG and PNG files are allowed.")

    if not image:
        raise ValidationError("Image is required.")


def clean_string(input_string: str) -> str:
    """
    Replace spaces with hyphens and strip special characters.
    """
    replaced = input_string.replace(" ", "-")
    return re.sub(r"[^\w\s-]", "", replaced)


def generate_unique_slug(model_instance, value, slug_field_name="slug"):
    """
    Generate a unique slug for a model instance.
    Example: "hello-world", "hello-world-1", "hello-world-2"
    """
    slug = slugify(value)
    unique_slug = slug
    model_class = model_instance.__class__
    counter = 1

    while model_class.objects.filter(**{slug_field_name: unique_slug}).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1

    return unique_slug
