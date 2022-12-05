from django.views.generic import ListView

from catalog.models import Item


class HomeView(ListView):
    model = Item
    template_name = 'homepage/homepage.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published().filter(is_on_main=True)
