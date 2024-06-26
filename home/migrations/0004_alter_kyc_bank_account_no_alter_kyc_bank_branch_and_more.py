# Generated by Django 4.1.2 on 2024-04-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kyc",
            name="bank_account_no",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="bank_branch",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="bank_ifsc",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="bank_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="bank_proof_file",
            field=models.FileField(
                blank=True, default="proof/myfile.pdf", null=True, upload_to="proof/"
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="proof_file",
            field=models.FileField(
                blank=True, default="proof/myfile.pdf", null=True, upload_to="proof/"
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="upi_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
