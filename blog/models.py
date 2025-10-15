from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150,
                                verbose_name="Заголовок",
                                blank=False,
                                null=False)

    content = models.TextField(verbose_name="Cодержание",
                               blank=False,
                               null=False)

    preview =models.ImageField(upload_to="images/",
                               verbose_name="Превью",
                               blank=True,
                               null=True)

    created_at = models.DateField(auto_now_add=True)

    is_published = models.BooleanField(verbose_name="Статус публикации")

    view_count = models.IntegerField(verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title}\n {self.content}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"