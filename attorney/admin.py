from django.contrib import admin
from .models import Attorney, Firm


class AttorneyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'pk',
        'number',
        'name',
        'email',
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
        # 'banner_image',
        'name',
        'phone',
        'email',
        'address',
        'working_hours',
    )

    list_editable = (
        'name',
        'phone',
        'email',
        'address',
        'working_hours',
    )


admin.site.register(Attorney, AttorneyAdmin)
admin.site.register(Firm, FirmAdmin)
