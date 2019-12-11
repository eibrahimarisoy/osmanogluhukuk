from django.db import models

DEFAULT_STATUS = "new"
# Create your models here.
STATUS = [
    # left side: DB
    # right side: human-readable name => DB de standart olması için soldaki bilgi DB için
    ('new', 'Yeni'),
    ('readed', 'Okundu'),
    ('deleted', 'Silindi'),
]

class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name="ad ve soyad")
    subject = models.CharField(max_length=50, verbose_name="Konu")
    email = models.EmailField(max_length=254, verbose_name="email")
    phone = models.IntegerField(verbose_name="telefon")
    content = models.TextField(verbose_name="mesaj")


    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  