# contacts/admin.py
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company_name', 'admin')
    list_filter = ('company_name', 'created_at')
    search_fields = ('full_name', 'email')
    readonly_fields = ('created_at',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admin=request.user)
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only set admin when creating
            obj.admin = request.user
        super().save_model(request, obj, form, change)