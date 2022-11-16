from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    template_name = 'catalog/item_list.html'
    item = Item.objects.item_list()
    context = {
        'items': item
    }
    return render(request, template_name, context)


def item_detail(request, pk=1):
    template_name = 'catalog/item_detail.html'
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item
    }
    return render(request, template_name, context)
