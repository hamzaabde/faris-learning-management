# Generated by Django 4.1.1 on 2022-09-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_courses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(help_text='Duration in hours', max_length=5),
        ),
    ]
