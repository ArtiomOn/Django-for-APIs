from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['id', 'author', 'title', 'body', 'created_at', 'updated_at']
