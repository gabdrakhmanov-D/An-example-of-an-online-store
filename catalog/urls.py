from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductListView, ContactFormView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductsCategoryListView

app_name = 'catalog'

urlpatterns = [
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    path("products/", ProductListView.as_view(), name="home"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path("products/add_product/", ProductCreateView.as_view(), name="add_product"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name='product_edit'),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name='product_delete'),
    path("category/<int:pk>/", ProductsCategoryListView.as_view(), name='category'),
]
