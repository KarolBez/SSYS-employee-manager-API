from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AgeReportView, SalaryReportView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reports/employees/age/', AgeReportView.as_view(), name='employee-age-report'),
    path('reports/employees/salary/', SalaryReportView.as_view(), name='employee-salary-report'),
]
