# Generated by Django 4.1.2 on 2024-07-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0027_contactus"),
    ]

    operations = [
        migrations.RenameField(
            model_name="p2prequestform",
            old_name="proof_choice",
            new_name="address_proof_choice",
        ),
        migrations.RenameField(
            model_name="p2prequestform",
            old_name="proof_file",
            new_name="address_proof_file",
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="address_proof_password",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="gps_location_proof_file",
            field=models.FileField(
                blank=True, default="proof/myfile.pdf", null=True, upload_to="proof/"
            ),
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="id_proof_choice",
            field=models.CharField(
                choices=[("aadhar", "aadhar"), ("pancard", "pancard")],
                default="aadhar",
                max_length=9,
            ),
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="id_proof_file",
            field=models.FileField(
                blank=True, default="proof/myfile.pdf", null=True, upload_to="proof/"
            ),
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="id_proof_password",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="income_proof_choice",
            field=models.CharField(
                choices=[("salaried", "salaried"), ("business", "business")],
                default="aadhar",
                max_length=9,
            ),
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="income_proof_file",
            field=models.FileField(
                blank=True, default="proof/myfile.pdf", null=True, upload_to="proof/"
            ),
        ),
        migrations.AddField(
            model_name="p2prequestform",
            name="income_proof_password",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
