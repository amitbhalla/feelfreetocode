# Generated by Django 3.2.6 on 2021-08-21 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coupon', '0002_coupon_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=150)),
                ('payment_id', models.CharField(max_length=150, null=True)),
                ('order_status', models.CharField(choices=[('S', 'Success'), ('F', 'Fail')], default='F', max_length=150)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('coupan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='coupon.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]