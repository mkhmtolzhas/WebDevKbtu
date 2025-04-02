from django.db import models

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='vacancies')
