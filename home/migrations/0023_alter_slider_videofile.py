# Generated by Django 4.1.2 on 2024-06-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0022_slider_videofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slider",
            name="videofile",
            field=models.FileField(
                null=True, upload_to="deploy/videos/", verbose_name="video"
            ),
        ),
    ]
