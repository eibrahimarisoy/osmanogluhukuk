from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from practice_area.models import PracticeArea
from blog.models import BlogPost

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'about', 'contact', 'attorneys', 'practice_areas', 'blogs']
    def location(self, item):
        return reverse(item)


class PracticeAreaSitemap(Sitemap):

    def items(self):
        return PracticeArea.objects.filter(status="published")

    def location(self, item):
        return reverse('single_practice_area', args=[item.slug])

class BlogPostSiteMap(Sitemap):

    def items(self):
        return BlogPost.objects.filter(status="published")
    
    def location(self, item):
        return reverse('blog_details', args=[item.slug])