from django.db import models
from django.utils import timezone


# Create your models here.

class Fayl_turi(models.Model):
    turi = models.CharField(max_length=250)

    def __str__(self):
        return self.turi


class Jurnallar(models.Model):
    class Status(models.TextChoices):
        qoralama = "QR","qoralama"
        chopetilish = "CHP", "chopetilish"
    nomi = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000)
    Text = models.TextField()
    rasm = models.ImageField(upload_to='news/images')
    fayl = models.FileField(upload_to='news/fayllar')
    chopetilishVaqti = models.DateTimeField(default=timezone.now)
    yaratilganVaqti = models.DateTimeField(auto_now_add=True)
    ozgarishVaqti = models.DateTimeField(auto_now=True)
    kategory = models.ForeignKey(Fayl_turi, on_delete=models.CASCADE)
    holati = models.CharField(max_length=3, choices=Status.choices, default=Status.qoralama)

    class Meta:
        ordering = ['-chopetilishVaqti']

    objects = models.Manager()

    def __str__(self):
        return self.nomi

class Yangiliklar(models.Model):
    class Status(models.TextChoices):
        qoralama = "QR","qoralama"
        chopetilish = "CHP", "chopetilish"
    nomi = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000)
    Text = models.TextField()
    rasm = models.ImageField(upload_to='news/images')
    chopetilishVaqti = models.DateTimeField(default=timezone.now)
    yaratilganVaqti = models.DateTimeField(auto_now_add=True)
    ozgarishVaqti = models.DateTimeField(auto_now=True)
    holati = models.CharField(max_length=3, choices=Status.choices, default=Status.qoralama)

    class Meta:
        ordering = ['-chopetilishVaqti']

    objects = models.Manager()

    def __str__(self):
        return self.nomi
