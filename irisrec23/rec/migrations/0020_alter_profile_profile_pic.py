# Generated by Django 4.1.2 on 2023-04-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0019_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='./media/users/user_avtar.webp', null=True, upload_to='users/'),
        ),
    ]
