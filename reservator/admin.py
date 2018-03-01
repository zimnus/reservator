from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

from ckeditor.widgets import CKEditorWidget
from django import forms

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


# Define a new FlatPageAdmin
class FlatPageAdminForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = FlatPage
        fields = "__all__"


class FlatPageAdmin(FlatPageAdmin):
    form = FlatPageAdminForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
