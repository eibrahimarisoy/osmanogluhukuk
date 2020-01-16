from django.db import models

# Create your models here.
DEFAULT_STATUS = "draft"
# Create your models here.
STATUS = [
    # left side: DB
    # right side: human-readable name => DB de standart olması için soldaki bilgi DB için
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class PracticeArea(models.Model):
    title = models.CharField(max_length=50, verbose_name="Çalışma Alanı")
    slug = models.SlugField(
        max_length=200, 
        default="",
        db_index=True,
    )
    content = models.TextField(verbose_name="İçerik")
    summary = models.CharField(max_length=250, default="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.")
    cover_image = models.FileField(blank=True, null=True, verbose_name="Fotoğraf")

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
        ordering = ["-created_date"]


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