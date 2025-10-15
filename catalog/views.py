from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView

from catalog.forms import ContactForm
from catalog.models import Product, StoreContact, Category
from django.template import loader


# Create your views here.

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
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('product_name')
#         description = request.POST.get('product_description')
#         image = request.FILES['product_image']
#         category_id = int(request.POST.get('product_category'))
#         category=Category.objects.get(pk=category_id)
#         purchase_price = request.POST.get('product_purchase_price')
#         Product.objects.create(name=name,
#                                description=description,
#                                image=image,
#                                category=category,
#                                purchase_price=purchase_price)
#         return render(request, 'catalog/thanks.html')
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     template = "catalog/add_product.html"
#     return render(request, template_name=template, context=context)
