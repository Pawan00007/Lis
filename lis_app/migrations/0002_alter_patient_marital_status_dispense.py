# Generated by Django 4.2 on 2023-04-28 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lis_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="Marital_Status",
            field=models.CharField(
                choices=[
                    ("S", "SINGLE"),
                    ("M", "MARRIED"),
                    ("D", "DIVORCED"),
                    ("O", "OTHERS"),
                ],
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Dispense",
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
                ("order_sequence_number", models.IntegerField()),
                ("dispense_sequence_number", models.IntegerField()),
                ("compound_code", models.CharField(max_length=100)),
                ("dispense_to_location", models.CharField(max_length=100)),
                ("dispense_to_address", models.CharField(max_length=100)),
                ("pharmacy_order_type", models.CharField(max_length=100)),
                ("original_order_date_time", models.DateTimeField()),
                ("give_per_time_unit", models.CharField(max_length=100)),
                ("give_rate_amount", models.CharField(max_length=100)),
                ("give_rate_units", models.CharField(max_length=100)),
                ("give_strength", models.IntegerField()),
                ("give_strength_units", models.CharField(max_length=100)),
                ("substance_lot_number", models.CharField(max_length=100)),
                ("substance_expiration_date", models.DateTimeField()),
                ("substance_manufacturer_name", models.CharField(max_length=100)),
                ("indication_for_use", models.CharField(max_length=100)),
                ("dispense_package_size", models.IntegerField()),
                (
                    "dispense_package_size_unit_of_measure",
                    models.CharField(max_length=100),
                ),
                ("dispense_package_method", models.CharField(max_length=100)),
                ("supplementary_code", models.CharField(max_length=100)),
                ("initiating_location", models.CharField(max_length=100)),
                ("packaging_assembly_location", models.CharField(max_length=100)),
                ("actual_drug_strength_volume", models.IntegerField()),
                ("actual_drug_strength_volume_units", models.CharField(max_length=100)),
                ("dispense_to_pharmacy_phone_number", models.CharField(max_length=100)),
                ("dispense_to_pharmacy_contact_name", models.CharField(max_length=100)),
                ("prescription_number", models.CharField(max_length=100)),
                ("number_of_refills_remaining", models.IntegerField()),
                ("dispense_notes", models.CharField(max_length=100)),
                ("dispensing_provider", models.CharField(max_length=100)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dispenses",
                        to="lis_app.patient",
                    ),
                ),
            ],
        ),
    ]
