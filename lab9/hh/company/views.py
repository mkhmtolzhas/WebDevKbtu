from .models import Company
from .serializers import CompanySerializer
from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def vacancies(self, request, pk=None):
        """
        Get all vacancies for a specific company.
        """
        company = self.get_object()
        vacancies = Vacancy.objects.filter(company=company)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


