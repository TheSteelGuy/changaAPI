# Generated by Django 2.2.1 on 2019-08-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0004_contribution_outstanding_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='first_name',
            new_name='checkout_request_id',
        ),
        migrations.RemoveField(
            model_name='contribution',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contribution',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='contribution',
            name='merchant_request_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='indicator_level',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
