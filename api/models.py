from django.db import models


# Create your models here.
class Vacancy(models.Model):
    url = models.URLField(primary_key=True)
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок')
    salary = models.CharField(max_length=50,
                              verbose_name='ЗП')
    company = models.CharField(max_length=255,
                               verbose_name='Компанія')
    recruiter = models.CharField(max_length=255,
                                 verbose_name='Рекрутер')
    publication_date = models.CharField(max_length=255,
                                        verbose_name='Дата публікації')
    views = models.IntegerField(verbose_name='Перегляди')
    reviews = models.IntegerField(verbose_name='Відгуки')
    short_description = models.CharField(max_length=255,
                                         verbose_name='Короткий опис')
    description = models.TextField(verbose_name='Опис')
    parse_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=True,
    )
