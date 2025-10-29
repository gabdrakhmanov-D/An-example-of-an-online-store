from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, DeleteView

from catalog.forms import ContactForm, ProductForm
from catalog.models import Product, StoreContact


class ProductListView(ListView):
    model = Product
    paginate_by = 3
    template_name = "catalog/home.html"
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_publish=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if not self.request.user.has_perm('product.can_unpublish_product'):
            data['form'].fields['is_publish'].disabled=True
            return data
        return data


    def form_valid(self, form):
        page = self.get_context_data()['object'].pk
        self.success_url = reverse_lazy("catalog:product_detail", kwargs={'pk': page})
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    def get_queryset(self, **kwargs):
        if not self.request.user.has_perm('product.delete_product'):
            raise PermissionDenied("У вас нет доступа для удаления товара.")

        return super().get_queryset()

    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")


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
