# Generated by Django 4.1.2 on 2023-04-23 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0003_branch_alter_profile_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='branch',
            new_name='name',
        ),
    ]
