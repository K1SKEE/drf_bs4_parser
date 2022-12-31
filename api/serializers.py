from rest_framework import serializers
from .models import Vacancy


class VacancyCreateSerializer(serializers.ModelSerializer):
    pass


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('url', 'title', )
