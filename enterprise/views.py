from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Enterprise, WORK_DAYS
from .forms import EnterpriseCreateForm
from employee.models import Employee
from account.models import ClientProfile
from django.contrib.auth.decorators import permission_required


# Create your views here.

########### NEW CODE #################

@login_required
def dashboard(request):
    template_name = 'enterprise/dashboard.html'
    template_data = {}
    return render(request, template_name, template_data)


@login_required
def enterprise(request):
    enterprises = Enterprise.objects.get_list(request.user)
    template_name = 'enterprise/enterprise_list.html'
    template_data = {'enterprises': enterprises}
    return render(request, template_name, template_data)


@login_required
def detail(request, pk):
    instance = Enterprise.objects.get(pk=pk)
    template_name = 'enterprise/enterprise_detail.html'
    template_data = {'instance': instance}
    return render(request, template_name, template_data)


@login_required
def create(request):
    if request.POST and request.FILES:
        form = EnterpriseCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_enterprise = form.save(commit=False)
            new_enterprise.owner = request.user
            new_enterprise.save()
            return HttpResponseRedirect('/')
    else:
        form = EnterpriseCreateForm()
    template_name = 'enterprise/create.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)
