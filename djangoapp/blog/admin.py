from typing import Any
from django.contrib import admin
from blog.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "id", "name", "slug",
    list_display_links = "name",
    search_fields = "id", "name", "slug",
    list_per_page = 10
    ordering = "-id",
    # prepopulate the slug field with the name inputed
    prepopulated_fields = {
        "slug": ("name",),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "slug",
    list_display_links = "name",
    search_fields = "id", "name", "slug",
    list_per_page = 10
    ordering = "-id",
    # prepopulate the slug field with the name inputed
    prepopulated_fields = {
        "slug": ("name",),
    }

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = "id", "title", "slug", "is_published",
    list_display_links = "title",
    search_fields = "id", "title", "slug", "is_published",
    list_per_page = 10
    list_filter = "is_published",
    list_editable = "is_published",
    ordering = "-id",
    prepopulated_fields = {
        "slug": ("title",),
    }

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = "id", "title", "is_published", "created_by",
    list_display_links = "title",
    search_fields = "id", "title", "slug", "excerpt", "content",
    list_per_page = 50
    list_filter = "category", "is_published",
    list_editable = "is_published",
    ordering = "-id",
    prepopulated_fields = {
        "slug": ("title",),
    }
    readonly_fields = "created_at", "updated_at", "created_by", "updated_by", 
    autocomplete_fields = "tags", "category",

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            
        obj.save()