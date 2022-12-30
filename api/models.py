from django.db import models


# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    recruiter = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    date = models.DateField()
    revision = models.IntegerField()
    response = models.IntegerField()
    url = models.URLField(primary_key=True)
    description = models.TextField()
    parse_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=True
    )
