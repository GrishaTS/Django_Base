from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import Feedback


def feedback(request):
    template_name = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        send_mail(
            f'Привет, {name}',
            'Мы получили вашу заявку, ожидайте ответа',
            'from@example.com',
            [email],
            fail_silently=True,
        )
        new_feedback = Feedback.objects.create(
            **form.cleaned_data
        )
        new_feedback.save()
        return redirect('feedback:feedback')
    return render(request, template_name, context)