from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateProfileForm, UpdateProfileForm
from .models import Profile


def signup(request):
    template_name = 'users/signup.html'
    form = CreateProfileForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('users:profile')
    return render(request, template_name, context)


def user_list(request):
    template_name = 'users/user_list.html'
    users = Profile.objects.is_activated()
    context = {
        'users_info': users,
    }
    return render(request, template_name, context)


def user_detail(request, pk):
    template_name = 'users/user_detail.html'
    user_info = get_object_or_404(
        Profile.objects.is_activated(),
        pk=pk,
    )
    context = {
        'user_info': user_info,
    }
    return render(request, template_name, context)


@login_required
def profile(request):
    template_name = 'users/profile.html'
    form = UpdateProfileForm(request.POST or None, instance=request.user)
    user_info = get_object_or_404(
        Profile,
        id=request.user.id,
    )
    context = {'form': form, 'user_info': user_info}
    if request.method == 'POST' and form.is_valid():
        Profile.objects.filter(id=request.user.id).update(
            **form.cleaned_data,
        )
        return redirect('users:profile')
    return render(request, template_name, context)
