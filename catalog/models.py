from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}\n {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField( verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/images', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара', blank=True, null=True, related_name= 'products')
    purchase_price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}\n {self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['purchase_price']
