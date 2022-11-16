from catalog.models import Item
from django.shortcuts import render


def home(request):
    template_name = 'homepage/homepage.html'
    item = Item.objects.published()
    context = {
        'items': item
    }
    return render(request, template_name, context)
