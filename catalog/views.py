from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product
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
        print(name,user_text)
        return render(request, 'catalog/thanks.html')
    return render(request, 'catalog/contacts.html')