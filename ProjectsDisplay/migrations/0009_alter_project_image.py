# Generated by Django 4.1.7 on 2023-06-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsDisplay', '0008_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]