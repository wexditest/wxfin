# Generated by Django 4.1.2 on 2024-04-10 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bug", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bug",
            name="assgined_to",
            field=models.CharField(
                blank=True,
                choices=[
                    ("DEEPAK", "DEEPAK"),
                    ("GEETHIKA", "GEETHIKA"),
                    ("SANGEETHA", "SANGEETHA"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]
