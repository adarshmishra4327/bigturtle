from django.contrib import admin
from blog.models import PostView, Author, Category, Comment, Post, Property

# Register your models here.
admin.site.register(PostView)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = "tinyinject.js"
