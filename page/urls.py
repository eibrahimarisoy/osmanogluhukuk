from django.urls import path
from .views import about, contact, attorneys, single_attorney, practice_areas, single_practice_area


urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('attorneys/', attorneys, name='attorneys'),
    path('attorneys/<slug:attorney_name>/', single_attorney, name='single_attorney'),
    path('practice_areas/', practice_areas, name='practice_areas'),
    path('practice_areas/<slug:practice_area_name>/', single_practice_area, name='single_practice_area'),


]