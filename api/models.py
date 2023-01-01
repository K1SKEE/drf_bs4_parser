from django.db import models


# Create your models here.

class VacancyManager(models.Manager):
    def create(self, vacancy_list):
        result = []
        for data in vacancy_list:
            vacancy = self.model(
                url=data.get('url'),
                title=data.get('title'),
                salary=data.get('salary'),
                company=data.get('company'),
                recruiter=data.get('recruiter'),
                publication_date=data.get('publication_date'),
                views=data.get('views'),
                reviews=data.get('reviews'),
                short_description=data.get('short_description'),
                description=data.get('description'),
                additional_info=data.get('additional_info')
            )
            vacancy.save()
            result.append(vacancy)
        return result


class Vacancy(models.Model):
    objects = VacancyManager()
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
    views = models.CharField(max_length=50,
                             verbose_name='Перегляди')
    reviews = models.CharField(verbose_name='Відгуки')
    short_description = models.CharField(max_length=255,
                                         verbose_name='Короткий опис')
    description = models.TextField(verbose_name='Опис')
    additional_info = models.JSONField(verbose_name='Додаткова інформація')
    parse_date = models.DateTimeField(
        auto_now_add=True
    )
