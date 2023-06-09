# Generated by Django 4.2 on 2023-04-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lis_app", "0003_machineinfo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="machineinfo",
            name="location",
        ),
        migrations.RemoveField(
            model_name="machineinfo",
            name="serial_number",
        ),
        migrations.AlterField(
            model_name="machineinfo",
            name="communication_direction",
            field=models.CharField(
                choices=[
                    ("unidirectional", "Unidirectional"),
                    ("bidirectional", "Bidirectional"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="machineinfo",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="machineinfo",
            name="port",
            field=models.CharField(
                choices=[("serial_port", "Serial_Port"), ("socket", "Socket")],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="machineinfo",
            name="protocol",
            field=models.CharField(
                choices=[("HL7", "HL7"), ("ASTM", "ASTM")], max_length=20
            ),
        ),
    ]
