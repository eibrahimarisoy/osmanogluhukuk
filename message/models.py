from django.db import models

DEFAULT_STATUS = "new"

STATUS = [
    ('new', 'Yeni'),
    ('readed', 'Okundu'),
    ('deleted', 'Silindi'),
]


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ad Soyad")
    subject = models.CharField(max_length=50, verbose_name="Konu")
    email = models.EmailField(max_length=254, verbose_name="Email")
    phone = models.CharField(max_length=11,verbose_name="Telefon")
    content = models.TextField(verbose_name="Mesaj")


    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
