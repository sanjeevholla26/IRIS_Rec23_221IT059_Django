# Generated by Django 4.1.2 on 2023-04-27 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0023_rename_cgpa_profile_student_cgpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cgpa',
            name='cgpa_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cutoff_cgpa', to='rec.branch'),
        ),
    ]
