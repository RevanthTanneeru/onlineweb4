# Generated by Django 2.1.9 on 2019-07-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0005_auto_20190713_2048"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="icon",
            field=models.URLField(
                blank=True,
                default="https://beta.online.ntnu.no/static/pwa-icon-v0-192.png",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="url",
            field=models.URLField(blank=True, default="/"),
        ),
    ]