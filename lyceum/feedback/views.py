from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import FeedbackForm
from .models import Feedback


class FeedBackView(FormView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/index.html'
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        send_mail(
            f'Привет, {name}',
            'Мы получили вашу заявку, ожидайте ответа',
            'from@example.com',
            [email],
            fail_silently=True,
        )
        form.save()
        return super().form_valid(form)
