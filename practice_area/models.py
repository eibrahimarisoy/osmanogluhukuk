from django.db import models
from ckeditor.fields import RichTextField

DEFAULT_STATUS = "draft"

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class CategoryPracticeArea(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, default="")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PracticeArea(models.Model):
    title = models.CharField(max_length=50, verbose_name="Çalışma Alanı")
    category = models.ForeignKey(
                    CategoryPracticeArea,
                    on_delete=models.CASCADE,
                    blank=True,
                    null=True
    )
    slug = models.SlugField(
        max_length=200, 
        default="",
        db_index=True,
    )
    content = RichTextField(verbose_name="İçerik")
    summary = models.CharField(
                    max_length=250,
                    default="Sed ut perspiciatis unde omnis iste natus \
                            error sit voluptatem accusantium doloremque \
                            laudantium, totam rem aperiam, eaque ipsa quae \
                            ab illo inventore veritatis et quasi architecto \
                            beatae vitae dicta sunt explicabo."
    )
    cover_image = models.FileField(
                    upload_to='practice_area',
                    blank=True,
                    null=True,
                    verbose_name="Fotoğraf"
    )
    number = models.IntegerField(unique=True, blank=True, null=True)
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
        ordering = ["number"]


class Faq(models.Model):
    question = models.CharField(max_length=250, verbose_name="Soru")
    answer = models.CharField(max_length=550, verbose_name="Cevap")
    
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

