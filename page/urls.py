from django.urls import path
from .views import about, contact, attorneys, practice_areas, single_practice_area
from .sitemaps import StaticViewSitemap, PracticeAreaSitemap, BlogPostSiteMap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
    'Çalışma Alanları': PracticeAreaSitemap,
    'Blog Yazıları': BlogPostSiteMap
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('attorneys/', attorneys, name='attorneys'),
    # path('attorneys/<slug:attorney_name>/', single_attorney, name='single_attorney'),
    path('practice-areas/', practice_areas, name='practice_areas'),
    path('practice-areas/<slug:practice_area_name>/', single_practice_area, name='single_practice_area'),

]