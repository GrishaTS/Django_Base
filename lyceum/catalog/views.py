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
    '''
    def get(self, request):
        form = self.form_class(
            initial=self.initial,
            instance=request.user,
        )
        context = {'form': form}
        return render(
            request,
            self.template_name,
            context,
        )'''
    def post(self, request, pk):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save(user_id=request.user.id, item_id=int(pk))
            return redirect('catalog:item_detail', pk)
        context = {'form': form}
        return render(request, self.template_name, context)
