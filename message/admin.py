from django.contrib import admin
from .models import Message
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'status',
        'name',
        'subject',
        'content',
        'email',
        'phone',
    )
    list_editable = (
        'status',
    )


admin.site.register(Message, MessageAdmin)