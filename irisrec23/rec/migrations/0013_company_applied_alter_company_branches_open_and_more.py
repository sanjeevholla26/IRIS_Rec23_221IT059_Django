# Generated by Django 4.1.2 on 2023-04-24 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rec', '0012_alter_company_branches_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='applied',
            field=models.ManyToManyField(blank=True, related_name='applied_company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='branches_open',
            field=models.ManyToManyField(blank=True, related_name='company', to='rec.branch'),
        ),
        migrations.AlterField(
            model_name='company',
            name='poc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_poc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('package', models.FloatField(blank=True, null=True)),
                ('student', models.ManyToManyField(blank=True, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='company', to='rec.posts'),
        ),
    ]
