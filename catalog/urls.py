from django.urls import path

from .views import ProductListView, ContactFormView, ProductDetailView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path("products/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    path("products/product_info/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path("products/add_product/", ProductCreateView.as_view(), name="add_product"),
]
