from django.contrib import admin
from .models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
    )
    list_filter = ('status',)
    list_editable = (
        'status',
    )

admin.site.register(BlogPost, BlogPostAdmin)