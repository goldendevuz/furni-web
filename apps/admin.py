from django.contrib import admin
# from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import User

from apps.models import Product


# Admin branding
admin.site.site_header = "Lumi"
admin.site.site_title = "Lumi's Admin Portal"
admin.site.index_title = "Welcome"


# Remove unused Group model
# admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("image", "name", "quantity", "is_quantity")

    def is_quantity(self, obj):
        """
        Show green check icon if quantity > 0, otherwise red cross icon.
        Compatible with Django 6.0+ (format_html requires args/kwargs).
        """
        if obj.quantity > 0:
            src = "https://img.icons8.com/color/30/checked--v1.png"
            alt = "in stock"
        else:
            src = "https://img.icons8.com/emoji/30/cross-mark-button-emoji.png"
            alt = "out of stock"

        return format_html(
            '<img width="30" height="30" src="{}" alt="{}" />',
            src,
            alt,
        )

    is_quantity.short_description = "In stock"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = tuple(f.name for f in User._meta.fields if f.name not in ('password', 'is_staff', 'is_superuser', 'id'))
    search_fields = ('username', 'email', 'phone')