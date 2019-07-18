# Generated by Django 2.2.1 on 2019-06-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaa', '0002_auto_20190628_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamaa',
            name='required_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='chamaa',
            name='contributions',
            field=models.ManyToManyField(to='contributions.Contribution'),
        ),
    ]
