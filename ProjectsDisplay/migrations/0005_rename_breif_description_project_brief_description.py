# Generated by Django 4.1.7 on 2023-06-18 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsDisplay', '0004_project_breif_description_alter_project_technology'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='breif_description',
            new_name='brief_description',
        ),
    ]