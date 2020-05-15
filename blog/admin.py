from django.contrib import admin
from .models import BlogPost, CategoryBlogPost


class BlogPostAdmin(admin.ModelAdmin): 
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'category',
        'status',
    )
    list_filter = ('status',)
    list_editable = (
        'status',
    )


class CategoryBlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(CategoryBlogPost, CategoryBlogPostAdmin)
