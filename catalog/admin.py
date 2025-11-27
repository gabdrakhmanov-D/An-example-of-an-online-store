from django.contrib import admin

from catalog.models import Product, Category, StoreContact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)


@admin.register(StoreContact)
class StoreContactAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email', 'main_office_address', 'office_hours', 'tg_contact',
                    'whatsapp',
                    'instagram',)
    search_fields = ('main_office_address', 'telephone',)
