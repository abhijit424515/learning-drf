# Generated by Django 4.2.1 on 2023-05-26 14:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("watchlist_app", "0003_watchlist_platform_alter_streamplatform_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                    "rating",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                ("description", models.CharField(max_length=300, null=True)),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                (
                    "watchlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="watchlist_app.watchlist",
                    ),
                ),
            ],
        ),
    ]