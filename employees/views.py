from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.db.models import Avg, Min, Max

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AgeReportView(generics.GenericAPIView):
    def get(self, request):
        employees = Employee.objects.all()
        youngest = employees.order_by('birth_date').first()
        oldest = employees.order_by('-birth_date').first()
        average_age = employees.aggregate(Avg('birth_date'))['birth_date__avg']
        data = {
            "younger": EmployeeSerializer(youngest).data,
            "older": EmployeeSerializer(oldest).data,
            "average": average_age.strftime('%Y-%m-%d') if average_age else None
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


