from django.contrib import admin
from .models import PracticeArea, Faq, CategoryPracticeArea
# Register your models here.
class PracticeAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'number',
        'title',
        'category',
        'slug',
        'status',
    )
    list_filter = ('status',)
    list_editable = (
        'status',
        'number',
    )


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'question',
        'answer',
        'status',
    )
    list_editable = (
        'status',
    )

class CategoryPracticeAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
    )


admin.site.register(PracticeArea, PracticeAreaAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(CategoryPracticeArea, CategoryPracticeAreaAdmin)