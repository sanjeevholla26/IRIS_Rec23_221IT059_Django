# Generated by Django 4.1.2 on 2023-04-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0011_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='branches_open',
            field=models.ManyToManyField(blank=True, null=True, related_name='company', to='rec.branch'),
        ),
    ]
