# Generated by Django 2.0.13 on 2019-05-06 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_magictoken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='magictoken',
            options={'default_permissions': ('add', 'change', 'delete')},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'default_permissions': ('add', 'change', 'delete')},
        ),
        migrations.AlterModelOptions(
            name='orderline',
            options={'default_permissions': ('add', 'change', 'delete')},
        ),
    ]