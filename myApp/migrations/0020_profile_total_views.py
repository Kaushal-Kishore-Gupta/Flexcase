# Generated by Django 4.1.6 on 2023-04-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0019_post_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="total_views",
            field=models.IntegerField(default=0),
        ),
    ]