from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField( verbose_name='Описание')
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=150, verbose_name='Категория')
    purchase_price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}\n {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['purchase_price']


class Category(models.Model):
    pass
