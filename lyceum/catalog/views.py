from django.shortcuts import render


def item_detail(request, pk=1):
    print(pk)
    if pk == '1':
        template_name = 'catalog/index_detail1.html'
    elif pk == '2':
        template_name = 'catalog/index_detail2.html'
    else:
        template_name = 'catalog/index_detail.html'
    return render(request, template_name)


def item_list(request):
    template_name = 'catalog/index.html'
    return render(request, template_name)
