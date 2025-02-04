from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_employee, name='add_employee'),  # Ensure this line exists
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('export/csv/', views.export_employees, name='export_csv'),
    path('export/excel/', views.export_employees_excel, name='export_excel'),
    path('import/', views.import_employees, name='import'),
    path('view/<int:employee_id>/', views.view_employee, name='view_employee'),
    path('employee/<slug:slug>/', views.view_employee, name='view_employee'),
]