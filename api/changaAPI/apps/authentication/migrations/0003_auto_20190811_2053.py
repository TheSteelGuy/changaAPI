# Generated by Django 2.2.1 on 2019-08-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_chamaas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contributions',
            field=models.ManyToManyField(blank=True, to='contributions.Contribution'),
        ),
    ]