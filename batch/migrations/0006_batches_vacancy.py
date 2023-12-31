# Generated by Django 4.2.4 on 2023-08-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("batch", "0005_alter_batches_days_alter_batches_teachername_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="batches",
            name="vacancy",
            field=models.CharField(
                choices=[("VACANT", "VACANT"), ("FULL", "FULL")],
                default="VACANT",
                max_length=50,
            ),
        ),
    ]
