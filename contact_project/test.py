from contacts.models import Employee
for emp in Employee.objects.all():
    print(emp.full_name, emp.slug)