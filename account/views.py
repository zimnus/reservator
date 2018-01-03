from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from enterprise.models import Enterprise
from .forms import RegisterForm, ProfileForm
from .models import ClientProfile

# Create your views here.

User = get_user_model()


# New code

def profile(request):
    user = request.user
    profile = ClientProfile.objects.get(user=user)
    owner_list = Enterprise.objects.get_list(profile.id)
    template_name = 'account/client_profile.html'
    template_data = {'user': user, 'profile': profile, 'owner_list': owner_list}
    return render(request, template_name, template_data)


def register(request, *args, **kwargs):
    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            group = form.cleaned_data['group']
            user, created = User.objects.get_or_create(username=username, first_name=first_name, last_name=last_name,
                                                       email=email)
            if created:
                user.set_password(password1)
                user.groups.add(group)
                user.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    template_name = 'account/register.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)


def edit(request):
    profile = ClientProfile.objects.get(user=request.user)
    if request.POST:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            edit_data = form.cleaned_data
            ClientProfile.objects.filter(user=request.user).update(**edit_data)
            return HttpResponseRedirect(reverse("account:profile"))
    else:
        form = ProfileForm(instance=profile)
    template_data = {'form': form, 'profile': profile}
    template_name = 'account/edit.html'
    return render(request, template_name, template_data)
