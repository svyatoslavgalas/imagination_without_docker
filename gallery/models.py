from django.db import models

from account.models import User
from .validators import validate_image


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images', verbose_name='Пользователь')
    image = models.ImageField('Изображение', validators=[validate_image])
    date_time = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='history', verbose_name='Картинка')
    old_path = models.ImageField('Изображение')
    date_time = models.DateTimeField(auto_now_add=True)
