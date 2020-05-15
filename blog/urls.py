from django.urls import path
from .views import blogs, blog_details


urlpatterns = [
    path('', blogs, name='blogs'),
    path('<slug:slug>/', blog_details, name="blog_details"),
]
