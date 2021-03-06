# Generated by Django 3.2.6 on 2021-08-21 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coupon", "0002_coupon_active"),
        ("order", "0002_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="coupan",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="coupon.coupon",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="coupan",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="coupon.coupon",
            ),
        ),
    ]
