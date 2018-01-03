from django.contrib import admin

from .models import OnlineBooking
# Register your models here.

@admin.register(OnlineBooking)
class OnlineBookingAdmin(admin.ModelAdmin):
    list_display = ('executor', 'enterprise', 'date', 'status', )
    search_fields = ('executor', 'enterprise', )
    ordering = ('date', 'status', )