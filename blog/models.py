from django.db import models
from ckeditor.fields import RichTextField

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

DEFAULT_STATUS = "draft"


class CategoryBlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, default="")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Başlık"
    )
    category = models.ForeignKey(
        CategoryBlogPost,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    content = RichTextField(verbose_name="İçerik")
    cover_image = models.FileField(
        upload_to='blog',
        blank=True,
        null=True,
        verbose_name="Fotoğraf"
    )
    author = models.CharField(max_length=255, null=True)
    slug = models.SlugField(
        max_length=200, 
        default="",
        db_index=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
