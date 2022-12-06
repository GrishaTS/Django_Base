from django.forms import Form, ChoiceField

from rating.models import Rating


class RatingForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    rate_field = ChoiceField(choices=Rating.Rate.choices)

    class Meta:
        fields = '__all__'
