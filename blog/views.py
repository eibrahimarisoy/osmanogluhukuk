from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def blogs(request):
    context = dict()
    blog_posts = BlogPost.objects.filter(
        status="published"
    )
    context['banner_page_name'] = "Blog Yazılarımız"

    paginator = Paginator(blog_posts, 9)
    page = request.GET.get("page", 1)
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        blog_posts = paginator.page(1)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)

    context['blog_posts'] = blog_posts
    return render(request, "page/blogs.html", context)

def blog_details(request, slug):
    context = dict()
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['banner_page_name'] = "Blog Yazılarımız"
    context['blog_post_title'] = blog_post.title

    context['blog_post'] = blog_post
    return render(request, "page/blog_details.html", context)