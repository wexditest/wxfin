# Generated by Django 4.1.2 on 2024-05-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_usefulllinks"),
    ]

    operations = [
        migrations.CreateModel(
            name="OneSlide",
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
                (
                    "summary_pic",
                    models.ImageField(default="avatar.jpg", upload_to="summary_pic/"),
                ),
            ],
        ),
    ]
