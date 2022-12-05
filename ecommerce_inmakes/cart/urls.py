from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('cart-items/', views.cartdetail, name="cart_detail"),
    path('add/<uuid:prod_id>/', views.add_cart, name="add_cart"),
    path('remove/<uuid:prod_id>/', views.cartitemremove, name="cart_item_remove"),
    path('clear/<uuid:prod_id>/', views.cartclear, name="cart_clear"),
]
