from django.core.cache import cache

from catalog.models import Product


def get_products_from_category(category_id):
    """ Функция для получения списка товаров из заданной категории """

    products = Product.objects.filter(category=category_id, is_publish=True)
    return products


def get_products_from_cache():
    """ Функция получает данные из кэша, если их нет делает запрос в БД """

    key = "products_list"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)
    return products