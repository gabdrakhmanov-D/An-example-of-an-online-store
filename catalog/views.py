from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, StoreContact, Category
from django.template import loader


# Create your views here.
def home(request):
    products = Product.objects.all()

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'catalog/home.html'
    context = {'products': products,
               'page_obj': page_obj,}

    return render(request, context=context, template_name=template)


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
    try:
        product = Product.objects.get(pk = product_id)
    except Product.DoesNotExist:
        product = None
    template = "catalog/product_info.html"
    context = {"product": product}
    return render(request, template_name=template, context=context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        image = request.FILES['product_image']
        category_id = int(request.POST.get('product_category'))
        category=Category.objects.get(pk=category_id)
        purchase_price = request.POST.get('product_purchase_price')
        Product.objects.create(name=name,
                               description=description,
                               image=image,
                               category=category,
                               purchase_price=purchase_price)
        return render(request, 'catalog/thanks.html')
    categories = Category.objects.all()
    context = {'categories': categories}
    template = "catalog/add_product.html"
    return render(request, template_name=template, context=context)
