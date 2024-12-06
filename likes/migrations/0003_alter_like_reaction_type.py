# Generated by Django 4.2 on 2024-10-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("likes", "0002_alter_like_unique_together_like_reaction_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="reaction_type",
            field=models.CharField(
                choices=[
                    ("heart", "Heart"),
                    ("thumbs_up", "Thumbs Up"),
                    ("laugh", "Laugh"),
                    ("sad", "Sad"),
                    ("angry", "Angry"),
                ],
                default="heart",
                max_length=10,
            ),
        ),
    ]
