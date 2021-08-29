# Generated by Django 3.2.6 on 2021-08-21 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coupon", "0002_coupon_active"),
        ("order", "0003_auto_20210821_1416"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="coupan",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="coupon.coupon",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="coupan",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="coupon.coupon",
            ),
        ),
    ]
