# Generated by Django 4.1.6 on 2023-04-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0017_remove_post_youtube_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="youtube_link",
            field=models.URLField(blank=True),
        ),
    ]
