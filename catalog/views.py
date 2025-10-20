from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView

from catalog.forms import ContactForm
from catalog.models import Product, StoreContact, Category


class HomeListView(ListView):
    model = Product
    paginate_by = 3
    template_name = "catalog/home.html"
    context_object_name = 'products'


class ContactFormView(FormView):
    template_name = "catalog/contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["store_contact"] = StoreContact.objects.all()[0]
        return context

    def form_valid(self, form):
        print(f'Имя пользователя: {form.cleaned_data["user_name"]}\n'
              f'Адрес электронной почты: {form.cleaned_data["user_email"]}\n'
              f'Сообщение: {form.cleaned_data["user_text"]}')
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name',
              'description',
              'image',
              'category',
              'purchase_price']
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
