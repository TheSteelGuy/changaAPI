# Generated by Django 2.2.1 on 2019-08-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
    ]
