# Generated by Django 2.2.1 on 2019-06-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaa', '0004_auto_20190619_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamaa',
            name='account_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
