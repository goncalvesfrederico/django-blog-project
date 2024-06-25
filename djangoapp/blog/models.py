from django.db import models
from utils.rands import new_slugfy
from django.contrib.auth.models import User

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
    
    def __str__(self) -> str:
        return self.name


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
    
    def __str__(self) -> str:
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length=80)
    slug = models.SlugField(
        unique=True,
        max_length=90,
        blank=True,
        default="",
        null=True,
    )
    is_published = models.BooleanField(
        default=False,
        help_text="This field needs to be checked for the page to be published."
    )
    content = models.TextField()

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = new_slugfy(self.title, 3)
        return super().save( *args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    title = models.CharField(max_length=80,)
    slug = models.SlugField(
        unique=True,
        max_length=120,
        blank=True,
        default="",
        null=True,
    )
    excerpt = models.CharField(max_length=120,)
    is_published = models.BooleanField(
        default=False,
        help_text="This field needs to be checked for the post to be published."
    )
    content = models.TextField()
    # post cover
    cover = models.ImageField(
        upload_to="posts/%Y/%m/",
        blank=True,
        default="",
    )
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text="If checked, it will display the cover within the post.",
    )
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="created_by",  # user.post_created_by.all
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="updated_by",  # user.post_updated_by.all
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        default="",
    )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        default="",
    )
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = new_slugfy(self.title, 3)
        return super().save( *args, **kwargs)
    
    def __str__(self) -> str:
        return self.title