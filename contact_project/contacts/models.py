from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Need to import reverse
from django.utils.text import slugify  # Add this import

class Employee(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)  # Admin who added the employee
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Keep null=True temporarily

    def save(self, *args, **kwargs):
        if not self.slug:
            # First save to get the ID
            super().save(*args, **kwargs)
            # Then create and save the slug
            self.slug = f"{slugify(self.full_name)}-{self.id}"
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_employee', kwargs={'slug': self.slug})

    def __str__(self):
        return self.full_name
    
    