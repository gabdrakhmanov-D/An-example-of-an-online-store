from . import views
from django.urls import path

from .views import HomeListView, ContactFormView

app_name = 'catalog'


urlpatterns = [
    # path('home/', views.home, name='home'),
    path("home/", HomeListView.as_view(), name="home"),
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    # path('contacts/', views.contacts, name='contacts'),
    path('product_info/<int:product_id>', views.product_info, name='product_info'),
    path('add_product/', views.add_product, name='add_product'),
]
