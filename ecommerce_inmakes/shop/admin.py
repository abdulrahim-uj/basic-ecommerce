from django.contrib import admin
from . models import CategoryModel, ProductModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'date_added']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CategoryModel, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'category',
                    'stock', 'available', 'date_added']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


admin.site.register(ProductModel, ProductAdmin)

