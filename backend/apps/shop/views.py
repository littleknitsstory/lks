from django.views.generic import ListView, DetailView

from .models.category import Category
from .models.product import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class CategoryProductsListView(ListView):
    model = Category
    template_name = 'category_products.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(
            category__slug=self.kwargs['slug'], active=True
        )
