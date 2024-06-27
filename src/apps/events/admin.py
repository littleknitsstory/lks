from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import OrderCart, OrderCartItem
from .models.category import Category, EventCategory
from .models.event import EventPhoto
from .models.product import Product, ProductPhoto, ProductColor


class AdminBaseMixin(admin.ModelAdmin):
    """Abstract model for shop admin"""

    list_display = ("pk", "title", "slug")
    save_as = True
    save_on_top = True

    class Meta:
        abstract = True


@admin.register(EventCategory)
class CategoryAdmin(TranslationAdmin, AdminBaseMixin):
    list_display = ("title", "slug", "created_at", "updated_at")
    fieldsets = (
        (_("Content"), {"fields": ("title",)}),
        (_("Main"), {"fields": ("slug",)}),
    )


class EventPhotoInline(admin.TabularInline):
    model = EventPhoto


@admin.register(EventPhoto)
class EventPhotoPhotoAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "image_alt")




@admin.register(Event)
class ProductAdmin(TranslationAdmin, AdminBaseMixin):
    inlines = [ProductPhotoInline]
    group_fieldsets = True
    list_display = ("id", "code", "slug", "is_active", "updated_at")
    list_display_links = ("slug")
    filter_horizontal = ("categories", )
    fieldsets = (
        (_("Title"), {"fields": ("title",)}),
        (
            _("Main"),
            {
                "fields": (
                    "slug",
                    "is_active",
                    "count",
                    "image_preview",
                    "author",
                    "categories",
                )
            },
        ),
        (_("Description"), {"fields": ("description",)}),
         (
            _("SEO"),
            {
                "fields": (
                    "meta_title",
                    "meta_keywords",
                    "meta_description",
                    "image_alt",
                )
            },
        ),
    )


class OrderCartItemInline(admin.TabularInline):
    model = OrderCartItem
    extra = 0
    readonly_fields = ("item_total_cost",)
    show_change_link = True


@admin.register(OrderCart)
class OrderCartAdmin(admin.ModelAdmin):
    inlines = [OrderCartItemInline]
    list_display = ("id", "order_number", "status", "updated_at", "created_at")
    list_display_links = ("order_number",)
    readonly_fields = ("updated_at", "created_at", "order_number", "order_total_cost")
    fieldsets = (
        (
            _("Status"),
            {
                "fields": (
                    "order_number",
                    "order_total_cost",
                    "status",
                    "updated_at",
                    "created_at",
                )
            },
        ),
        (
            _("Info"),
            {"fields": ("email", "phone", "address", "comments")},
        ),
    )


@admin.register(OrderCartItem)
class OrderCartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order_cart", "product", "amount")
    fieldsets = ((_("Info"), {"fields": ("order_cart", "product", "amount")}),)
