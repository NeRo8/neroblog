from django.contrib import admin

# Register your models here.
from blog.models import Post, Comment, Like


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')


def make_draft(modeladmin, request, queryset):
    queryset.update(status='draft')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post_id', 'comment_text', 'author', 'date_pub')
    list_filter = ('date_pub', 'author')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'user', 'date_create')
    list_filter = ('date_create',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_pub', 'likeit', 'status')
    actions = [make_published, make_draft]
