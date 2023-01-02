from rest_framework import generics
from rest_framework.response import Response

from .serializers import *


# Create your views here.
class VacancyParseAPIView(generics.CreateAPIView):
    serializer_class = VacancyParseSerializer

    def post(self, request, *args, **kwargs):
        serializer = VacancyParseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vacancy = serializer.create(serializer.data)
        return Response({})


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


class VacancyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer
