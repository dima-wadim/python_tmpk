# Generated by Django 5.0.3 on 2024-03-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tmpk", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adres",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sity", models.CharField(max_length=35, verbose_name="Город")),
                ("strit", models.CharField(max_length=50, verbose_name="Улица")),
                (
                    "hom_nambe",
                    models.CharField(max_length=50, verbose_name="Номер дома"),
                ),
                (
                    "hom",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Номер квартиры",
                    ),
                ),
            ],
            options={
                "verbose_name": "Адрес",
                "verbose_name_plural": "Адрес",
            },
        ),
    ]
