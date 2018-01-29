from django.contrib import admin
from .models import StaffSchedule


# Register your models here.

@admin.register(StaffSchedule)
class StaffScheduleAdmin(admin.ModelAdmin):
    list_display = ('staff', 'is_work', 'work_date', )
