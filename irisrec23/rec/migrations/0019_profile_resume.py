# Generated by Django 4.1.2 on 2023-04-27 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0018_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
