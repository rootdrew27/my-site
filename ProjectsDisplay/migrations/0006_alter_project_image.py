# Generated by Django 4.1.7 on 2023-06-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsDisplay', '0005_rename_breif_description_project_brief_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='./ProjectsDisplay/static/img'),
        ),
    ]
