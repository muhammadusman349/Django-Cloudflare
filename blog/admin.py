from django.contrib import admin
from .models import BlogPost
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'timestamp')
    list_filter = ('id', 'title')


admin.site.register(BlogPost, BlogPostAdmin)