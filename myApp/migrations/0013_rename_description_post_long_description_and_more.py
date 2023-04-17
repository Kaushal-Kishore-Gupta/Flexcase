# Generated by Django 4.1.6 on 2023-04-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0012_profile_firstsetting"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="description",
            new_name="long_description",
        ),
        migrations.AddField(
            model_name="post",
            name="short_description",
            field=models.TextField(default="Short Description"),
        ),
    ]