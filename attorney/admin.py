from django.contrib import admin
from .models import Attorney
# Register your models here.
class AttorneyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'pk',
        'name',
        'slug',
        'position',
        'status',
    )
    list_filter = ('status',)
    list_editable = (
        'status',
    )










admin.site.register(Attorney, AttorneyAdmin)