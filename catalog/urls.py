from django.urls import path

from .views import HomeListView, ContactFormView, ProductDetailView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path("home/", HomeListView.as_view(), name="home"),
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    path("product_info/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path("add_product/", ProductCreateView.as_view(), name="add_product"),
]
