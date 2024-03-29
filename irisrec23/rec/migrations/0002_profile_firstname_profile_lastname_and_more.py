# Generated by Django 4.1.2 on 2023-04-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='register_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(max_length=50),
        ),
    ]
