from django.db.models import Avg
from django.shortcuts import redirect, render
from django.views.generic import DetailView, FormView, ListView

from .models import Item


def item_list(request):
    template_name = 'catalog/item_list.html'
    items = Item.objects.published().order_by('category__name', 'name')
    context = {
        'items': items,
    }
    return render(request, template_name, context)


def item_detail(request, pk=1):
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'

    def get(self, request, pk):
        form = self.form_class(
            request.POST or None,
            initial={'rate': 3},
        )
        user = request.user
        item = Item.objects.get(pk=pk)
        if user.is_authenticated:
            rate = Rating.objects.filter(
                user=user,
                item=item,
            )
            if rate:
                rate = rate.get(
                    user=user,
                    item=item,
                )
                form['rate'].initial = rate.rate
        average_rating = Rating.objects.filter(
            item=item
        ).aggregate(Avg('rate'))
        number_of_ratings = Rating.objects.filter(
            item=item
        ).count()
        context = {
            'form': form,
            'item': item,
            'rate_count': number_of_ratings,
            'rate': average_rating,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = request.user
            item = Item.objects.get(pk=pk)
            obj = form.save(commit=False)
            Rating.objects.update_or_create(
                user=user,
                item=item,
                defaults={
                    'rate': obj.rate,
                },
            )
            return redirect('catalog:item_detail', pk)
        context = {'form': form}
        return render(request, self.template_name, context)
