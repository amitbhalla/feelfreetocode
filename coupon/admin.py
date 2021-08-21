from django.contrib import admin

from coupon.models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ["course", "code", "discount", "active"]
    ordering = ["course", "code", "discount"]
    readonly_fields = ("id", "code")
    list_editable = ("active",)


admin.site.register(Coupon, CouponAdmin)
