from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enterprise.models import Enterprise
from .models import Category, Service
from .forms import ServiceCreateForm

# Create your views here.

@login_required
def service(request):
    categories = Category.objects.filter(enterprise__owner=request.user)
    services = Service.objects.all()
    template_name = 'service/list.html'
    template_data = {'categories': categories, 'services': services}
    return render(request, template_name, template_data)


@login_required
def create_category(request):
    template_name = 'service/category_create.html'
    template_data = {}
    return render(request, template_name, template_data)


@login_required
def create_service(request):
    form = ServiceCreateForm()
    template_name = 'service/service_create.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)
