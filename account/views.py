from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from enterprise.models import Enterprise
from .forms import RegisterForm, ProfileForm, ClientCreateForm, EnterpriseManagerForm
from .models import ClientProfile

from django.views.generic import FormView

# Create your views here.

User = get_user_model()


# New code
@login_required
def profile(request):
    user = request.user
    if user.client:
        profile = ClientProfile.objects.get(user=user)
    elif user.manager:
        profile = Enterprise.objects.get(owner=user)
    else:
        profile = user
    template_name = 'account/profile.html'
    template_data = {'profile': profile}
    return render(request, template_name, template_data)


def register(request, *args, **kwargs):
    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password(password1)
                user.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    template_name = 'account/register.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)


class CreateClientView(FormView):
    template_name = 'account/client_create.html'
    form_class = ClientCreateForm
    success_url = '/'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateClientView, self).get_context_data(**kwargs)
        return context


class CreateManagerView(FormView):
    template_name = 'account/manager_create.html'
    success_url = '/'
    form_class = EnterpriseManagerForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
