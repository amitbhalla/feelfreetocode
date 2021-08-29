import uuid

from django.db import models
from django.contrib.auth.models import User

from coupon.models import Coupon
from course.models import Course

order_status_choices = (
    ("S", "Success"),
    ("F", "Fail"),
)


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    order_id = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=True)
    order_status = models.CharField(
        max_length=150, default="F", choices=order_status_choices
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders"
    )
    time = models.DateTimeField(auto_now_add=True)
    coupan = models.ForeignKey(
        Coupon,
        on_delete=models.CASCADE,
        related_name="orders",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.order_id)


class OrderItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="order_items"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    coupan = models.ForeignKey(
        Coupon,
        on_delete=models.CASCADE,
        related_name="order_items",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.course)


class Subscription(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="subscriptions"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="subscriptions"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    time = models.DateTimeField(auto_now_add=True)
