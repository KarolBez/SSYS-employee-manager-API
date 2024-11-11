from rest_framework import viewsets, generics
from rest_framework.response import Response
from datetime import date
from django.db.models.functions import ExtractYear
from .models import Employee
from django.utils import timezone
from django.db.models import F, ExpressionWrapper, IntegerField
from .serializers import EmployeeSerializer
from django.db.models import Avg, Min, Max


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AgeReportView(generics.GenericAPIView):
    def get(self, request):
        employees = Employee.objects.all()
        today = date.today()

        # Calcula a idade de cada funcionário considerando apenas o ano atual e o ano de nascimento
        employees_with_age = employees.annotate(
            age=today.year - ExtractYear(F('birth_date'))
        )

        youngest = employees_with_age.order_by('age').first()
        oldest = employees_with_age.order_by('-age').first()
        average_age = round(employees_with_age.aggregate(average_age=Avg('age'))['average_age'], 2)

        data = {
            "younger": EmployeeSerializer(youngest).data,
            "older": EmployeeSerializer(oldest).data,
            "average": average_age
        }
        return Response(data)
    
class SalaryReportView(generics.GenericAPIView):
    def get(self, request):
        employees = Employee.objects.all()
        min_salary = employees.order_by('salary').first()
        max_salary = employees.order_by('-salary').first()
        average_salary = employees.aggregate(Avg('salary'))['salary__avg']
        data = {
            "lowest": EmployeeSerializer(min_salary).data,
            "highest": EmployeeSerializer(max_salary).data,
            "average": f"{average_salary:.2f}" if average_salary else None
        }
        return Response(data)


