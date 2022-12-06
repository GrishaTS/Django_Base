from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import Profile


class CreateProfileForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
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
        model = Profile
        fields = ('email', 'birthday', 'first_name', 'last_name')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
