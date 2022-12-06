from django.views.generic import DetailView, ListView, FormView
from django.shortcuts import redirect, render

from catalog.models import Item
from rating.forms import RatingForm


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

    def post(self, request, pk):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            data['user_id'] = request.user.id
            data['item_id'] = pk
            print(data)
            rate = Item(**data)
            print(rate)
            rate.save()
            return redirect('catalog:item_detail', pk)
        context = {'form': form}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
