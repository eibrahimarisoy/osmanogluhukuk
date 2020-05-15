from django.urls import path
from .views import about, contact, attorneys, practice_areas, \
     practice_area_details, attorney_details
from .sitemaps import StaticViewSitemap, PracticeAreaSitemap, \
     BlogPostSiteMap, AttorneySiteMap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
    'Çalışma Alanları': PracticeAreaSitemap,
    'Blog Yazıları': BlogPostSiteMap,
    'Ekibimiz': AttorneySiteMap,
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('attorneys/', attorneys, name='attorneys'),
    path('attorneys/<slug:attorney_name>/', attorney_details, name='attorney_details'),
    path('practice-areas/', practice_areas, name='practice_areas'),
    path('practice-areas/<slug:practice_area_name>/',
         practice_area_details,
         name='practice_area_details'),
]
