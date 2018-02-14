from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from reservator.models import User


class CustomUserAdmin(UserAdmin):
    # readonly_fields = ('ga_uid', 'ga_cid')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'image', 'phone', 'manager', 'client')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # change_form_template = 'admin/user_form.html'


admin.site.register(User, CustomUserAdmin)
