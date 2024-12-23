# Generated by Django 4.2 on 2024-10-28 20:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0002_post_image_filter"),
        ("likes", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="like",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="like",
            name="reaction_type",
            field=models.CharField(
                choices=[
                    ("heart", "Heart"),
                    ("thumps_up", "Thumps Up"),
                    ("laugh", "Laugh"),
                    ("sad", "Sad"),
                    ("angry", "Angry"),
                ],
                default="heart",
                max_length=10,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("owner", "post", "reaction_type")},
        ),
    ]
