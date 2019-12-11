from django.contrib import admin
from .models import PracticeArea
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










admin.site.register(PracticeArea, PracticeAreaAdmin)