# Generated by Django 5.0.4 on 2024-05-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="todoModel",
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
                ("task_title", models.CharField(max_length=50)),
                ("is_done", models.BooleanField(default=False)),
            ],
        ),
    ]
