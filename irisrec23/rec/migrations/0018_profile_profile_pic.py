# Generated by Django 4.1.2 on 2023-04-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0017_alter_cgpa_cgpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
