from django.db import models

# Create your models here.
DEFAULT_STATUS = "draft"

STATUS = [
    # left side: DB
    # right side: human-readable name => DB de standart olması için soldaki bilgi DB için
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]
 

class Carousel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
        help_text="1920*700 px boyutunda resim yükleyiniz",
    )
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


