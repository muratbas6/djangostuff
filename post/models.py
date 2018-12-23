from django.db import models

# Create your models here.

class yazi(models.Model):
    başlık = models.CharField(max_length=120)
    metin = models.TextField()
    yayinTarihi = models.DateTimeField()

    def __str__(self):
        return self.başlık