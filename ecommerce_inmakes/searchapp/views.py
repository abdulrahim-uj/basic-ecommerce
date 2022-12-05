from django.shortcuts import render
from shop.models import ProductModel
from django.db.models import Q


def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = ProductModel.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query))
        context = {
            'query': query,
            'products': products,
        }
        return render(request, 'searchapp/search.html', context=context)

