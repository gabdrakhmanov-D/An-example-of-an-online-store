from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView

# from .views import ProductListView, ContactFormView, ProductDetailView, ProductCreateView, ProductUpdateView, \
#     ProductDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', next_page='catalog:home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),]
