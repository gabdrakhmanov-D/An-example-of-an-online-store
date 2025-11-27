from django.db import models

from users.models import User


class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}\n {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="images/", verbose_name="Изображение", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория товара",
        related_name="users",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор записи",
        related_name="products",
    )
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    is_publish = models.BooleanField(default=False, verbose_name="Статус публикации")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}\n {self.description}"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["purchase_price"]
        permissions = [
            ("can_unpublish_product", "Сan unpublish product"),

        ]


class StoreContact(models.Model):

    telephone = models.CharField(max_length=20, verbose_name="Телефон для связи")
    email = models.CharField(max_length=50, verbose_name="Электронная почта")
    main_office_address = models.CharField(max_length=200, verbose_name="Адрес офиса")
    office_hours = models.CharField(max_length=200, verbose_name="Время работы офиса")
    tg_contact = models.CharField(max_length=50, verbose_name="Телеграмм")
    whatsapp = models.CharField(max_length=50, verbose_name="Ватсапп")
    instagram = models.CharField(max_length=50, verbose_name="Инстаграмм", blank=True, null=True)

    def __str__(self):
        return f"{self.main_office_address}\n {self.telephone}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
