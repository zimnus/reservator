from django.contrib import admin

from .models import Category, Service


# Register your models here.

class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1


@admin.register(Category)
class CategoryOfServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'enterprise',)
    inlines = [ServiceInline, ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'enterprise', )
