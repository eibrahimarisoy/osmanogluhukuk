from django.contrib import admin
from .models import PracticeArea, Faq
# Register your models here.
class PracticeAreaAdmin(admin.ModelAdmin):
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

admin.site.register(PracticeArea, PracticeAreaAdmin)
admin.site.register(Faq, FaqAdmin)