# Generated by Django 2.2.3 on 2019-07-15 23:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import common.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=common.models.user_directory_path,
                    ),
                ),
                ("bio", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        )
    ]