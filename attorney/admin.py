from django.contrib import admin
from .models import Attorney, Firm
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

class FirmAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
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