from django.db import models


DEFAULT_STATUS = "draft"
# Create your models here.
STATUS = [
    # left side: DB
    # right side: human-readable name => DB de standart olması için soldaki bilgi DB için
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class Attorney(models.Model):
    name = models.CharField(max_length=50, verbose_name="ad ve soyad")
    slug = models.SlugField(
        max_length=200, 
        default="",
        db_index=True,
    )
    position = models.CharField(max_length=50, verbose_name="pozisyon")
    cover_image = models.FileField(blank=True, null=True,verbose_name="fotoğraf 600*700px")
    profile = models.TextField(verbose_name="özgeçmiş")
    email = models.EmailField(max_length=254, verbose_name="email")
    phone = models.IntegerField(verbose_name="telefon")

    number = models.IntegerField(unique=True, blank=True, null=True)

    facebook = models.CharField(max_length=100, verbose_name="facebook", blank=True, null=True)
    twitter = models.CharField(max_length=100, verbose_name="twitter", blank=True, null=True)
    instagram = models.CharField(max_length=100, verbose_name="instagram", blank=True, null=True)
    linkedin = models.CharField(max_length=100, verbose_name="linkedin", blank=True, null=True)

    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-number']    

class Firm(models.Model):
    name = models.CharField(max_length=250, verbose_name="Firma Adı")
    address = models.CharField(max_length=250, verbose_name="Adres")
    phone = models.IntegerField(verbose_name="Telefon")
    email = models.EmailField(max_length=254, verbose_name="Email")
    working_hour = models.CharField(max_length=150, verbose_name="Çalışma Saatleri")
    cover_image = models.ImageField(upload_to="logo", verbose_name="200*75 px", blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name