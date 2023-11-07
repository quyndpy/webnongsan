from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Customer, Cart, Wishlist, OrderPlayced, Payment
from django.urls import reverse


# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'mobile', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']


@admin.register(Payment)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'order_id', 'payment_status', 'payment_id', 'paid']

@admin.register(OrderPlayced)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']