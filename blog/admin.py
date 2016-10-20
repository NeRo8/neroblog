from django.contrib import admin

# Register your models here.
from blog.models import Post, Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'date_pub', 'author')
    list_filter = ('date_pub',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'user', 'date_create')
    list_filter = ('date_create',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_pub', 'likeit', 'status')
