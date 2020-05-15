from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from page.views import index
from message.views import message_submit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('', include('page.urls'),),
    path('blogs/', include('blog.urls')),
    path('message_submit/', message_submit, name='message_submit'),
    path('media/(<path>)', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static/(<path>)', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'page.views.error_404_view'
