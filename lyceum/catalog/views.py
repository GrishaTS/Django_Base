from django.views.generic import DetailView, ListView, FormView
from django.shortcuts import redirect, render

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

    def get(self, request, pk):
        form = self.form_class(request.POST or None)
        rate = Rating.objects.get(
            user=request.user,
            item=Item.objects.get(pk=pk)
        )
        if rate:
            form['rate'].initial = rate.rate
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.item = Item.objects.get(pk=pk)
            Rating.objects.filter(
                user=obj.user, item=obj.item
            ).update_or_create(rate=obj.rate)
            return redirect('catalog:item_detail', pk)
        context = {'form': form}
        return render(request, self.template_name, context)
