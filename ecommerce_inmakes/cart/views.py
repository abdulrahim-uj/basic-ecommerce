from django.shortcuts import render, redirect, get_object_or_404
from shop.models import ProductModel
from . models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# CREATE CART ID WITH SESSION ID
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, prod_id):
    product = ProductModel.objects.get(pk=prod_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    return redirect('cart:cart_detail')


def cartdetail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart/cart.html',
                  dict(cartitems=cart_items, total=total, counter=counter))


def cartitemremove(request, prod_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(ProductModel, id=prod_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def cartclear(request, prod_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(ProductModel, id=prod_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
