from django.db import models
from shop.models import ProductModel, CategoryModel
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    cart_id = models.CharField(max_length=128, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'cart_cart'
        ordering = ['-date_added']
        verbose_name = _('cart')
        verbose_name_plural = _('carts')

    def __str__(self):
        return '{}'.format(self.cart_id)


class CartItem(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart_cart_item'
        verbose_name = _('cart_item')
        verbose_name_plural = _('cart_items')

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)

