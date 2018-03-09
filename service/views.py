from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

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
def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.filter(enterprise__owner=request.user).exclude(pk=category.pk)
    services = Service.objects.filter(service=category)
    template_name = 'service/category_detail.html'
    template_data = {'category': category, 'categories': categories, 'services': services}
    return render(request, template_name, template_data)


@login_required
def service_detail(request, service_id):
    services = Service.objects.get(pk=service_id)
    template_name = 'service/service_detail.html'
    template_data = {'services': services}
    return render(request, template_name, template_data)


@login_required
def service_update(request, service_id):
    enterprise = Enterprise.objects.get(owner=request.user)
    instance = Service.objects.get(pk=service_id)
    if request.POST:
        form = ServiceCreateForm(enterprise, request.POST or None, instance=instance)
        if form.is_valid():
            update_data = form.cleaned_data
            Service.objects.filter(pk=service_id).update(**update_data)
            return HttpResponseRedirect(reverse('service:service'))
    else:
        form = ServiceCreateForm(enterprise, instance=instance)
    template_name = 'service/service_update.html'
    template_data = {'service': instance, 'form': form}
    return render(request, template_name, template_data)


def create_category_ajax(request):
    return JsonResponse('Success!')
