from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Vacancy
from .utils import parse_vacancies


class VacancyParseSerializer(serializers.Serializer):
    url = serializers.URLField()
    parse_pages = serializers.IntegerField()

    def create(self, validated_data):
        vacancies = parse_vacancies(
            link=validated_data.get('url'),
            parse_pages=validated_data.get('parse_pages')
        )
        result = []
        for vacancy in vacancies:
            try:
                href = vacancy.get('href')
                Vacancy.objects.get(pk=href)
            except ObjectDoesNotExist:
                result.append(Vacancy.objects.create(vacancy))
        return result


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ('description', 'parse_date')


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
