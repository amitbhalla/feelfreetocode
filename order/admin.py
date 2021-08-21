from django.contrib import admin

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order_id",
        "payment_id",
        "order_status",
        "user",
        "time",
    ]
    ordering = ["user", "order_id"]
    readonly_fields = ("id",)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "course",
        "order",
        "price",
        "discount",
        "time",
    ]
    ordering = ["course", "price"]
    readonly_fields = ("id",)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
