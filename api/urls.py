from django.urls import path

from .views import *

urlpatterns = [
    path('parse/', VacancyParseAPIView.as_view()),
    path('list/', VacancyListAPIView.as_view()),
    path('detail/<str:pk>/', VacancyRetrieveAPIView.as_view())

]
