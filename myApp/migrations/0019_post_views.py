# Generated by Django 4.1.6 on 2023-04-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0018_post_youtube_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]