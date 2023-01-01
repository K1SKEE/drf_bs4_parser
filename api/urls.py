from django.urls import path

from .views import *

urlpatterns = [
    path('parse/', VacancyParseAPIView.as_view()),
    path('short/', VacancyListAPIView.as_view()),

]
