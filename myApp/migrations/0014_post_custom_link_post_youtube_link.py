# Generated by Django 4.1.6 on 2023-04-17 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0013_rename_description_post_long_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="custom_link",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="post",
            name="youtube_link",
            field=models.URLField(blank=True),
        ),
    ]