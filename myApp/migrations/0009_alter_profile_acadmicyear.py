# Generated by Django 4.1.6 on 2023-03-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0008_rename_other_profile_twitter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="acadmicyear",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
