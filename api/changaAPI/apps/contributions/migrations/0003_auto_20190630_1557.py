# Generated by Django 2.2.1 on 2019-06-30 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0002_auto_20190630_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='indicator_value',
            new_name='indicator_level',
        ),
    ]