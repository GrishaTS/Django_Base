from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView

from users.forms import CreateProfileForm, UpdateProfileForm
from users.models import Profile


class SignUpView(FormView):
    template_name = 'users/signup.html'
    model = Profile
    form_class = CreateProfileForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = Profile
    context_object_name = 'users_info'
    get_queryset = Profile.objects.is_activated


class UserDetailView(DetailView):
    template_name = 'users/user_detail.html'
    model = Profile
    context_object_name = 'user'


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    form_class = UpdateProfileForm
    model = Profile
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['form'].errors:
            context['form'] = self.form_class(
                initial=self.initial,
                instance=self.request.user,
            )
        return context

    def form_valid(self, form):
        self.model.objects.filter(id=self.request.user.id).update(
            **form.cleaned_data,
        )
        return super().form_valid(form)
