"""osmanogluhukuk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from page.views import index
from message.views import message_submit
from django.conf.urls import handler404
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('', include('page.urls'),),
    path('blogs/', include('blog.urls')),
    path('message_submit/', message_submit, name='message_submit'),
    path('media/(<path>)', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static/(<path>)', serve,{'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'page.views.error_404_view'