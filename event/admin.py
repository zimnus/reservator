from django.contrib import admin

from .models import Event


# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('staff', 'client', 'start_date', 'start_time',)
