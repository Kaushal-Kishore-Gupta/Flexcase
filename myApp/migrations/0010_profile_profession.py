# Generated by Django 4.1.6 on 2023-04-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0009_alter_profile_acadmicyear"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profession",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
