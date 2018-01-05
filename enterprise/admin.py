from django.contrib import admin
from .models import Enterprise, City
from employee.models import Employee, CategoryOfServices


# Register your models here.

class EmployyInline(admin.StackedInline):
    model = Employee
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title',)
    search_fields = ('title',)
    inlines = [EmployyInline, ]


@admin.register(CategoryOfServices)
class CategoryOfServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'enterprise',)
