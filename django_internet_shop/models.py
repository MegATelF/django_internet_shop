from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    username = models.CharField(_("Имя"), max_length=100, unique=True)
    email = models.EmailField(_("Эл. Почта"))
    password = models.CharField(_("Пароль"), max_length=100)

    def __str__(self):
        return self.username

class Item(models.Model):
    title = models.CharField(_("Имя"), max_length=100)
    author = models.CharField(_("Автор"),max_length=100)
    pages = models.IntegerField(_("Кол-во страниц"),)
    genre =  models.CharField(_("Жанр"),max_length=100)
    publish_date = models.DateField(_("Дата публикации"),)
    description = models.TextField(_("Описание"),)
    price = models.DecimalField(_("Цена"),max_digits=6, decimal_places=2)
    count = models.IntegerField(_("Кол-во на складе"),)
    image = models.ImageField(_('Изображение'), upload_to='images/', blank=True, null=True, default='images/default.jpg')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Книга")
        verbose_name_plural = _("Книги")

class User(models.Model):
    username = models.CharField(_("Имя"), max_length=100)
    email = models.EmailField(_("Эл. Почта"))
    password = models.CharField(_("Пароль"), max_length=100)

    def __str__(self):
        return self.username
    
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='Item')
    quantity = models.PositiveIntegerField(default=1)
    

