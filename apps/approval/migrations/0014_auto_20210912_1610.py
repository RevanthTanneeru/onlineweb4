# Generated by Django 3.0.14 on 2021-09-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("approval", "0013_manual_m2m_to_through"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membershipapproval",
            name="field_of_study",
            field=models.IntegerField(
                choices=[
                    (0, "Gjest"),
                    (1, "Bachelor i Informatikk"),
                    (10, "Programvaresystemer"),
                    (11, "Databaser og søk"),
                    (12, "Algoritmer og datamaskiner"),
                    (13, "Spillteknologi"),
                    (14, "Kunstig intelligens"),
                    (15, "Helseinformatikk"),
                    (16, "Interaksjonsdesign, spill- og læringsteknologi"),
                    (30, "Annen mastergrad"),
                    (40, "Sosialt medlem"),
                    (80, "PhD"),
                    (90, "International"),
                    (100, "Annet Onlinemedlem"),
                ],
                default=0,
                verbose_name="studieretning",
            ),
        ),
    ]