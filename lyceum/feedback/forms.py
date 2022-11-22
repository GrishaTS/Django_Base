from django import forms
from django.core.exceptions import ValidationError

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.startswith('a'):
            raise ValidationError('Имя должно начинаться на "a"')
        return name

    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'Имя',
        }
