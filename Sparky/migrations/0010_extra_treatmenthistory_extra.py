# Generated by Django 5.1.1 on 2025-01-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Sparky", "0009_alter_treatmenthistory_appointment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Extra",
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
                    "extraName",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="ค่าใช้จ่ายเพิ่มเติม"
                    ),
                ),
                ("price", models.FloatField(blank=True, null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="treatmenthistory",
            name="extra",
            field=models.ManyToManyField(
                blank=True, to="Sparky.extra", verbose_name="ค่าใช้จ่ายเพิ่มเติม"
            ),
        ),
    ]
