from django.contrib import admin
from .models import Attorney, Firm
# Register your models here.
class AttorneyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'pk',
        'number',
        'name',
        'slug',
        'position',
        'status',
    )
    list_filter = ('status',)
    list_editable = (
        'number',
        'status',

    )

class FirmAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'cover_image',
        'name',
        'phone',
        'email',
        'address',
        'working_hour',
    )

    list_editable = (
        'name',
        'phone',
        'email',
        'address',
        'working_hour',
    )









admin.site.register(Attorney, AttorneyAdmin)
admin.site.register(Firm, FirmAdmin)