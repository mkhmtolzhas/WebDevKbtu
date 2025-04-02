from .models import Vacancy
from .serializers import VacancySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class VacancyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vacancies to be viewed or edited.
    """
    queryset = Vacancy.objects.all().order_by('-id')
    serializer_class = VacancySerializer

    @action(detail=False, methods=['get'])
    def top_ten(self, request, pk=None):
        """
        Get the top 10 vacancies based on salary.
        """
        top_vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(top_vacancies, many=True)
        return Response(serializer.data)

    