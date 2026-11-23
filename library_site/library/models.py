from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=100)
    year = models.IntegerField("Год издания")
    pages = models.IntegerField("Страниц")
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField("Добавлена", auto_now_add=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.title} — {self.author}"

    def get_absolute_url(self):
        return reverse("library:book_detail", args=[self.pk])
