# Generated by Django 4.1.2 on 2023-04-28 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0028_posts_open_time_alter_posts_open_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='open_date',
        ),
    ]