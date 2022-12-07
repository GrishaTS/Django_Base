from django.db.models import Avg, Count
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView

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

    def get_success_url(self):
        return reverse_lazy(
            'catalog:item_detail',
            args=(
                self.kwargs['pk'],
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rating = Rating.objects.filter(
            item=context['item'],
        )
        context['stat'] = rating.aggregate(
            Avg('rate'),
            Count('rate'),
        )
        if self.request.user and self.request.user.is_authenticated:
            rate = rating.filter(
                user=self.request.user,
            ).first()
            if rate:
                context['form'].fields['rate'].initial = rate.rate
        return context

    def post(self, request, pk):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            if not form.cleaned_data['rate']:
                Rating.objects.filter(user=request.user.id, item=pk).delete()
            else:
                Rating.objects.update_or_create(
                    user_id=request.user.id,
                    item_id=pk,
                    defaults={
                        'rate': form.cleaned_data['rate'],
                    },
                )
        return super().post(self, request)
