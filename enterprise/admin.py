from django.contrib import admin
from .models import Enterprise, City
from employee.models import Employee


# Register your models here.

class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'created_at', 'updated_at', )
    search_fields = ('title',)
    inlines = [EmployeeInline, ]
