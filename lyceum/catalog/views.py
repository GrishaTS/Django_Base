from catalog.models import Item
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, FormView, ListView
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

    # def get(self, request, pk): переписать!!!
    #     form = self.form_class()
    #     user = request.user
    #     item = get_object_or_404(
    #         Item.objects.published(),
    #         pk=pk,
    #     )
    #     if user.is_authenticated:
    #         rate = Rating.objects.filter(
    #             user=user,
    #             item=item,
    #         )
    #         if rate:
    #             rate = rate.get(
    #                 user=user,
    #                 item=item,
    #             )
    #             form['rate'].initial = rate.rate
    #     average_rating = Rating.objects.filter(
    #         item=item
    #     ).aggregate(Avg('rate'))
    #     number_of_ratings = Rating.objects.filter(
    #         item=item
    #     ).count()
    #     context = {
    #         'form': form,
    #         'item': item,
    #         'rate_count': number_of_ratings,
    #         'rate': average_rating,
    #     }
    #     return render(request, self.template_name, context)

    # def post(self, request, pk):
    #     form = self.form_class(request.POST or None)
    #     if form.is_valid():
    #         user = request.user
    #         item = Item.objects.get(pk=pk)
    #         rate = form.save(commit=False).rate
    #         if rate is None:
    #             Rating.objects.filter(user=user, item=item).delete()
    #         else:
    #             Rating.objects.update_or_create(
    #                 user=user,
    #                 item=item,
    #                 defaults={
    #                     'rate': rate,
    #                 },
    #             )
    #         return redirect('catalog:item_detail', pk)
    #     context = {'form': form}
    #     return render(request, self.template_name, context)