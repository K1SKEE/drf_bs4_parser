from django.db import models


# Create your models here.

class VacancyManager(models.Manager):
    def create(self, data):
        vacancy = self.model(
            href=data.get('href'),
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
            # additional_info=data.get('additional_info')
        )
        vacancy.save()
        return vacancy


class Vacancy(models.Model):
    objects = VacancyManager()
    href = models.CharField(primary_key=True,
                            max_length=255)
    url = models.URLField()
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок')
    salary = models.CharField(max_length=255,
                              verbose_name='ЗП',
                              null=True)
    company = models.CharField(max_length=255,
                               verbose_name='Компанія',
                               null=True)
    recruiter = models.CharField(max_length=255,
                                 verbose_name='Рекрутер')
    publication_date = models.CharField(max_length=255,
                                        verbose_name='Дата публікації')
    views = models.CharField(max_length=255,
                             verbose_name='Перегляди')
    reviews = models.CharField(max_length=255,
                               verbose_name='Відгуки')
    short_description = models.TextField(verbose_name='Короткий опис')
    description = models.TextField(verbose_name='Опис')
    # additional_info = models.JSONField(verbose_name='Додаткова інформація',
    #                                    null=True)
    parse_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-publication_date']
