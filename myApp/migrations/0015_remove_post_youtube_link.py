# Generated by Django 4.1.6 on 2023-04-17 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0014_post_custom_link_post_youtube_link"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="youtube_link",
        ),
    ]
