from django.contrib import admin
from django.urls import path
from api import views  # Importando as views do seu aplicativo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.employee_list, name='employee_list'),
    path('reports/employees/age/', views.age_range_report, name='age_range_report'),
    path('reports/employees/salary/', views.salary_range_report, name='salary_range_report'),
]
