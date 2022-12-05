from django.contrib import admin
from . models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'active']
    list_editable = ['quantity', 'active']
    # prepopulated_fields = {'slug': ('name',)}
    # list_per_page = 10


admin.site.register(CartItem, CartItemAdmin)