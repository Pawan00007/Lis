# Generated by Django 4.2 on 2023-04-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lis_app", "0004_remove_machineinfo_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machineinfo",
            name="communication_direction",
            field=models.CharField(
                blank=True,
                choices=[
                    ("unidirectional", "Unidirectional"),
                    ("bidirectional", "Bidirectional"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="machineinfo",
            name="protocol",
            field=models.CharField(
                choices=[
                    ("HL7", "HL7"),
                    ("ASTM", "ASTM"),
                    ("DICOM", "DICOM"),
                    ("NCPDP", "NCPDP"),
                    ("FHIR", "FHIR"),
                    ("X12", "X12"),
                    ("CDA", "CDA"),
                ],
                max_length=20,
            ),
        ),
    ]
