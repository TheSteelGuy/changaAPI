# Generated by Django 2.2.1 on 2019-08-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamaa', '0003_auto_20190630_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamaa',
            name='contributions',
            field=models.ManyToManyField(blank=True, to='contributions.Contribution'),
        ),
    ]
