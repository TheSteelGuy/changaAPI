# Generated by Django 2.2.1 on 2019-06-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='indicator_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='contribution',
            name='required_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]