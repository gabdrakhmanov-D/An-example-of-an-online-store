from . import views
from django.urls import path

from .views import HomeListView, ContactFormView, ProductDetailView

app_name = 'catalog'


urlpatterns = [
    # path('home/', views.home, name='home'),
    path("home/", HomeListView.as_view(), name="home"),
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    path("product_info/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
]
