from django.contrib import admin

from .models import ClientProfile
from enterprise.models import Enterprise


# Register your models here.

class EnterpriseInline(admin.StackedInline):
    model = Enterprise
    extra = 1


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'contact_email',)
    # inlines = [EnterpriseInline]
