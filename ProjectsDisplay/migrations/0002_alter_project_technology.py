# Generated by Django 4.1.7 on 2023-06-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsDisplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=40),
        ),
    ]
