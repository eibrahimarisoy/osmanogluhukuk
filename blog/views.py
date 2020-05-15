from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blogs(request):
    context = dict()
    blog_posts = BlogPost.objects.filter(status="published")

    paginator = Paginator(blog_posts, 9)
    page = request.GET.get("page", 1)
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        blog_posts = paginator.page(1)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)

    context['banner_page_name'] = "Blog Yazılarımız"
    context['blog_posts'] = blog_posts
    return render(request, "page/blogs.html", context)


def blog_details(request, slug):
    context = dict()
    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_posts = BlogPost.objects.filter(
        status="published",
        category=blog_post.category
    ).exclude(id=blog_post.id)

    context['banner_page_name'] = "Blog Yazılarımız"
    context['blog_post_title'] = blog_post.title
    context['blog_post'] = blog_post
    context['blog_posts'] = blog_posts
    return render(request, "page/blog_details.html", context)
