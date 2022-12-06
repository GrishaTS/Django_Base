from django.forms import ModelForm, Select

from rating.models import Rating


class RatingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Rating
        fields = '__all__'
        exclude = ('user', 'item',)
