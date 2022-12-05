import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey("auth.User", blank=True,
                                related_name="creator_%(class)s_objects",
                                on_delete=models.CASCADE)
    updater = models.ForeignKey("auth.User", blank=True,
                                related_name="updator_%(class)s_objects",
                                on_delete=models.CASCADE)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_close = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CategoryModel(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="Categories/", blank=True)

    class Meta:
        db_table = 'shop_category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('-date_added', 'name')

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class ProductModel(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Products/", blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        db_table = 'shop_product'
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('-date_added', 'name')

    def get_url(self):
        return reverse('shop:product_category_detail',
                       args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
