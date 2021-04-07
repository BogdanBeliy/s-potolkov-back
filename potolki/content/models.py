from django.db import models
from PIL import Image

# Create your models here.


class Cards(models.Model):
    imgUrl = models.ImageField(default="", upload_to="images/cards/")
    name = models.CharField(max_length=15)
    descr = models.TextField()

    class Meta:
        verbose_name = 'Карточки потолков'
        verbose_name_plural = 'Карточки потолков'


class Testimonials(models.Model):
    testimonialImg = models.ImageField(upload_to="testimonials/", default="")
    text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery/")
    title = models.TextField(
        default="Изготовление и монтаж натяжных потолков в Минске и минской области | s-potolkov | s potolkov | spotolok")


class NewClient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    area = models.IntegerField(default="")
    dot_light = models.IntegerField(default="")
    potolok = models.CharField(max_length=300)


class NewSalePotolok(models.Model):
    type_sale = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    potolok = models.CharField(max_length=35)

    def __str__(self):
        return self.name
