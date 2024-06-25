from django.db import models
from utils.rands import new_slugfy

class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=80)
    slug = models.SlugField(
        unique=True,
        max_length=90,
        blank=True,
        default="",
        null=True,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = new_slugfy(self.name, 3)
        return super().save( *args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=80)
    slug = models.SlugField(
        unique=True,
        max_length=90,
        blank=True,
        default="",
        null=True,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = new_slugfy(self.name, 3)
        return super().save( *args, **kwargs)