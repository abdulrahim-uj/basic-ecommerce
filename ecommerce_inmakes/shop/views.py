from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import CategoryModel, ProductModel
# PAGINATOR
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allProdCat(request, cat_slug=None):
    cat_page = None
    products_list = None
    if cat_slug != None:
        cat_page = get_object_or_404(CategoryModel, slug=cat_slug)
        products_list = ProductModel.objects.all().filter(category=cat_page, available=True)
        paginator = Paginator(products_list, per_page=6)
        try:
            page_data = int(request.GET.get('page', '1'))
        except:
            page_data = 1
        try:
            products = paginator.page(page_data)
        except (EmptyPage, InvalidPage):
            products = paginator.page(paginator.num_pages)
        context = {
            'category': cat_page,
            'products': products,
        }
        return render(request, "categories/category.html", context=context)
    else:
        products_list = ProductModel.objects.all().filter(available=True)
        paginator = Paginator(products_list, per_page=6)
        try:
            page_data = int(request.GET.get('page', '1'))
        except:
            page_data = 1
        try:
            products = paginator.page(page_data)
        except (EmptyPage, InvalidPage):
            products = paginator.page(paginator.num_pages)
        context = {
            'category': cat_page,
            'products': products,
        }
        return render(request, "categories/category.html", context=context)


def productDetail(request, cat_slug, prod_slug):
    try:
        product = ProductModel.objects.get(category__slug=cat_slug, slug=prod_slug)
    except Exception as e:
        raise e
    context = {
        'product': product
    }
    return render(request, "products/product.html", context=context)
