from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.allProdCat, name="allprodcat"),
    path('<slug:cat_slug>/', views.allProdCat, name="products_by_category"),
    path('<slug:cat_slug>/<slug:prod_slug>/', views.productDetail,
         name="product_category_detail"),
]
