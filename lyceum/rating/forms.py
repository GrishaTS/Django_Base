from django.forms import ModelForm, ChoiceField

from rating.models import Rating


class RatingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    def save(self, user_id=None, item_id=None):
        self.item = int(item_id)
        self.user = user_id
        super().save()

    class Meta:
        model = Rating
        fields = ('rate',)
