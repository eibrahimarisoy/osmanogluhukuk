from django.contrib import admin
from .models import Carousel
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'content',
        'status',
    )
    list_filter = ('status',)
    list_editable = (
        'status',
    )
admin.site.register(Carousel, CarouselAdmin)