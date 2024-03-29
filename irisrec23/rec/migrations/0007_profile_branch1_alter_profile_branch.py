# Generated by Django 4.1.2 on 2023-04-23 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rec', '0006_alter_profile_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='branch1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
