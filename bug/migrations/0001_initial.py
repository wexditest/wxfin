# Generated by Django 4.1.2 on 2024-03-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bug",
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
                    "bug_phase",
                    models.CharField(
                        blank=True,
                        choices=[("US", "US"), ("ISSUE", "ISSUE"), ("OTHER", "OTHER")],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("bug_title", models.CharField(blank=True, max_length=80, null=True)),
                ("bug_detail", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "priority",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("HIGH", "HIGH"),
                            ("MEDIUM", "MEDIUM"),
                            ("LOW", "LOW"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("NOTSTARTED", "NOT-STARTED"),
                            ("INPROGRESS", "IN-PROGRESS"),
                            ("FIXED", "FIXED"),
                            ("HOLD", "HOLD"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("WEBSITE", "WEBSITE"),
                            ("MOBILEAPP", "MOBILEAPP"),
                            ("BUSINESS", "BUSINESS"),
                            ("TOOLS", "TOOLS"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "issue_pic",
                    models.ImageField(
                        default="bugissue/default/no-img.jpg", upload_to="bugissue/"
                    ),
                ),
                (
                    "assgined_to",
                    models.CharField(
                        blank=True,
                        choices=[("DEEPAK", "DEEPAK")],
                        max_length=10,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
