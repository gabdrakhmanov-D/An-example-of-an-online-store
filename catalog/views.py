from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, StoreContact
from django.template import loader


# Create your views here.
def home(request):
    latest_added_product = Product.objects.order_by('-created_at')[:5]
    template = loader.get_template("catalog/home.html")
    context = {"latest_added_product": latest_added_product}
    for product in latest_added_product:
        print(f'Название: {product.name}\n'
              f'Описание: {product.description}\n')
    return HttpResponse(template.render(context, request))


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        user_text = request.POST.get('user_text')
        print(name, user_text)
        return render(request, 'catalog/thanks.html')
    store_contact = StoreContact.objects.all()[0]
    template = loader.get_template("catalog/contacts.html")
    context = {"store_contact": store_contact}
    return HttpResponse(template.render(context, request))


def product_info(request, product_id):
    product = Product.objects.get(product_id)
    template = "catalog/product_info.html"
    context = {"product_info": product}
    return render(request, template_name=template, context=context)
