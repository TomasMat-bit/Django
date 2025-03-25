from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at')
    list_filter = ('created_at', 'post')
    search_fields = ('author_name', 'content')




