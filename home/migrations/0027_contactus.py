# Generated by Django 4.1.2 on 2024-06-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0026_expenseslist"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("phone", models.CharField(blank=True, max_length=100, null=True)),
                ("subject", models.CharField(blank=True, max_length=100, null=True)),
                ("message", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
