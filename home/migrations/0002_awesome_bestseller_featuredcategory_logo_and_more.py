# Generated by Django 4.2.7 on 2023-12-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="awesome",
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
                ("name", models.CharField(max_length=300, unique=True)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                ("url", models.URLField(blank=True, max_length=500)),
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="bestseller",
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
                ("name", models.CharField(max_length=300, unique=True)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                ("url", models.URLField(blank=True, max_length=500)),
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="featuredcategory",
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
                ("name", models.CharField(max_length=300, unique=True)),
                ("logo", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300, unique=True)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                ("url", models.URLField(blank=True, max_length=500)),
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="logo",
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
                ("name", models.CharField(max_length=300, unique=True)),
                ("logo", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300, unique=True)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="subscription",
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
                ("name", models.CharField(max_length=300, unique=True)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                ("url", models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="weeklysale",
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
                ("name", models.CharField(max_length=300, unique=True)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                ("url", models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name="category",
        ),
    ]
