from django.db import migrations
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    Employee = apps.get_model('contacts', 'Employee')
    for emp in Employee.objects.all():
        emp.slug = f"{slugify(emp.full_name)}-{emp.id}"
        emp.save()

class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0001_initial'),  # Must match your initial migration
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]