# Generated by Django 3.1.1 on 2020-09-30 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registerItem', '0002_auto_20200819_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='device',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='registerItem.stock'),
        ),
    ]
