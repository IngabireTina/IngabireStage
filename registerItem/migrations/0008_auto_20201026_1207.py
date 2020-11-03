# Generated by Django 3.1.2 on 2020-10-26 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registerItem', '0007_stock_userrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='userRecord',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
