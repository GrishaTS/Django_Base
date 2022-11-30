from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

User = get_user_model()


class CreateProfileForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }


class UpdateProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    password = None

    class Meta:
        model = User
        fields = ('email', 'birthday', 'first_name', 'last_name')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
