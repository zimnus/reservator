from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from enterprise.models import Enterprise
from .forms import RegisterForm, ProfileForm
from .models import ClientProfile

# Create your views here.

User = get_user_model()


# New code


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
