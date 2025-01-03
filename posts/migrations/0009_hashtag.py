# Generated by Django 4.2 on 2024-11-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0008_alter_post_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hashtag",
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
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "posts",
                    models.ManyToManyField(
                        blank=True, related_name="hashtags", to="posts.post"
                    ),
                ),
            ],
        ),
    ]
