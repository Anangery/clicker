# Generated by Django 4.2.2 on 2023-06-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clickersite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='times',
            name='dtime',
            field=models.TimeField(),
        ),
    ]
