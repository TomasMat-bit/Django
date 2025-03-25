from django.contrib import admin
from .models import Post, Comment, Author, Book

admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at')
    list_filter = ('created_at', 'post')
    search_fields = ('author_name', 'content')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_date')
    list_filter = ('author', 'release_date')

admin.site.register(Author)
admin.site.register(Book, BookAdmin)



