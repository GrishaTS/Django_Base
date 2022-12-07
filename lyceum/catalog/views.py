from django.db.models import Avg, Count
from django.views.generic import DetailView, FormView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from catalog.models import Item
from rating.forms import RatingForm
from rating.models import Rating


class ItemListView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    get_queryset = Item.objects.published


class ItemDetailView(DetailView, FormView):
    model = Item
    form_class = RatingForm
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'

    def get_success_url(self, pk):
        return reverse_lazy('catalog:item_detail', pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stat'] = Rating.objects.filter(
            item=context['item'],
        ).aggregate(Avg('rate'), Count('rate'))
        return context

    def post(self, request, pk):
        form = self.form_class(request.POST or None)
        item = Item.objects.get(pk=pk)
        if form.is_valid():
            Rating.objects.update_or_create(
                user=request.user,
                item=item,
                defaults={
                    'rate': form.cleaned_data['rate'],
                },
            )
        return redirect('catalog:item_detail', pk)
