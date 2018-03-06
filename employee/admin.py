from django.contrib import admin

from employee.models import Position, Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')
    ordering = ['-weight', ]
